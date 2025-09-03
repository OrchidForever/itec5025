import tensorflow as tf
import csv
from routes.index import ROUTES
from slots.media_slots import fill_slots_for_intent, extract_add_media_slots, missing_slots, ask_for, get_intent_from_response

# Load model + vectorizer + response map
model = tf.keras.models.load_model("data/chatbot_model.keras")
vectorizer_model = tf.keras.models.load_model("data/vectorizer.keras")

vectorizer = vectorizer_model.layers[1]


index_to_response = {}
with open('data/processed_convo_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        index_to_response[int(row['index'])] = row['response']


# Chat loop
def chatbot():
    print("Chatbot ready! Type 'quit' to exit.")
    dialog_state = {"intent": None, "slots": {}, "awaiting": None}
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == 'quit':
            break


        if dialog_state["awaiting"] and dialog_state["intent"] == "add_media":
            slot = dialog_state["awaiting"]
            val = extract_add_media_slots(user_input).get(slot) or user_input
            dialog_state["slots"][slot] = val
            dialog_state["awaiting"] = None
            need = missing_slots("add_media", dialog_state["slots"])
            if need:
                dialog_state["awaiting"] = need[0]
                print("Bot:", ask_for(need[0], "add_media"))
                continue
            res = ROUTES["add_media"]["fn"](**dialog_state["slots"])
            print("Bot:", res)
            dialog_state = {"intent": None, "slots": {}, "awaiting": None}
            continue

        vec_input = vectorizer([user_input])
        pred = model.predict(vec_input)
        response_index = tf.argmax(pred, axis=1).numpy()[0]
        print(f"[DEBUG] Predicted class index: {response_index}")
        
        # Determine intent from user input directly
        intent = get_intent_from_response(user_input)

        if intent != "add_media":
            # handle your other intents / canned responses as before
            if response_index in index_to_response:
                print("Bot:", index_to_response[response_index])
            else:
                print("Bot: I'm not sure how to help with that.")
            continue

        # New add_media turn: fill what we can, then ask for missing
        slots = fill_slots_for_intent("add_media", user_input)
        dialog_state["intent"] = "add_media"
        dialog_state["slots"].update({k: v for k, v in slots.items() if v})

        need = missing_slots("add_media", dialog_state["slots"])
        if need:
            dialog_state["awaiting"] = need[0]
            print("Bot:", ask_for(need[0], "add_media"))
        else:
            res = ROUTES["add_media"]["fn"](**dialog_state["slots"])
            print("Bot:", res)
            dialog_state = {"intent": None, "slots": {}, "awaiting": None}

chatbot()
