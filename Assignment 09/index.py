import tensorflow as tf
import csv
from routes.index import ROUTES
from slots.media_slots import fill_slots_for_intent, extract_add_media_slots, missing_slots, ask_for

# Load model + vectorizer + response map
model = tf.keras.models.load_model("data/chatbot_model.keras")
vectorizer_model = tf.keras.models.load_model("data/vectorizer.keras")

vectorizer = vectorizer_model.layers[1]


index_to_response = {}
with open('data/processed_convo_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        index_to_response[int(row['index'])] = row['response']

intent_index_to_name = {
    0: "add_media", 
    1: "search_media",
    2: "update_media_status",
}

# Chat loop
def chatbot():
    print("Chatbot ready! Type 'quit' to exit.")
    dialog_state = {"intent": None, "slots": {}, "awaiting": None}
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == 'quit':
            break

    
        if dialog_state["awaiting"] and dialog_state["intent"] in ROUTES:
            slot = dialog_state["awaiting"]
            val = extract_add_media_slots(user_input).get(slot) or user_input
            dialog_state["slots"][slot] = val
            dialog_state["awaiting"] = None
            need = missing_slots(dialog_state["intent"], dialog_state["slots"])
            if need:
                dialog_state["awaiting"] = need[0]
                print("Bot:", ask_for(need[0], dialog_state["intent"]))
                continue
            res = ROUTES[dialog_state["intent"]]["fn"](**dialog_state["slots"])
            print("Bot:", res)
            dialog_state = {"intent": None, "slots": {}, "awaiting": None}
            continue

        vec_input = vectorizer([user_input])
        pred = model.predict(vec_input)
        predicted_intent = tf.argmax(pred, axis=1).numpy()[0]
        print(f"[DEBUG] Predicted class index: {predicted_intent}")
        print(f"[DEBUG] Model confidence: {pred[0][predicted_intent]:.4f}")
        # Determine intent from user input directly
        intent = intent_index_to_name.get(predicted_intent, "chitchat")

        # New add_media turn: fill what we can, then ask for missing
        slots = fill_slots_for_intent(intent, user_input)
        dialog_state["intent"] = intent
        dialog_state["slots"].update({k: v for k, v in slots.items() if v})

        need = missing_slots(intent, dialog_state["slots"])
        if need:
            dialog_state["awaiting"] = need[0]
            print("Bot:", ask_for(need[0], intent))
        else:
            res = ROUTES[intent]["fn"](**dialog_state["slots"])
            print("Bot:", res)
            dialog_state = {"intent": None, "slots": {}, "awaiting": None}

chatbot()
