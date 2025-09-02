import tensorflow as tf
import csv
from routes.index import ROUTES
import re

# Load model + vectorizer + response map
model = tf.keras.models.load_model("data/chatbot_model.keras")
vectorizer_model = tf.keras.models.load_model("data/vectorizer.keras")

vectorizer = vectorizer_model.layers[1]


index_to_response = {}
with open('data/processed_convo_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        index_to_response[int(row['index'])] = row['response']

PROMPTS = {
    ("add_media", "name"): "What's the media name? (you can put it in quotes)",
    ("add_media", "owner"): "Who is the owner?",
    ("add_media", "location"): "Where is it located? (URL, file path, or bucket URI)",
}
def ask_for(slot, intent): 
    return PROMPTS.get((intent, slot), f"I need {slot}:")

URL_RE = re.compile(r'\b((?:https?://|s3://|gs://|wasbs://)[^\s]+)', re.I)
PATH_RE = re.compile(r'(?<!\w)(?:[A-Za-z]:\\[^:*?"<>|]+|/[^ \t\n\r]+(?:/[^ \t\n\r]+)*)')
BUCKET_RE = re.compile(r'\b(?:s3|gs)://[^\s]+', re.I)

def extract_name(text: str):
    # "Quoted Title"
    q = re.search(r'"([^"]{2,200})"', text)
    if q:
        return q.group(1).strip()
    # Title Case chunk (at least two words starting with caps)
    m = re.search(r'\b([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+){1,6})\b', text)
    if m:
        return m.group(1).strip()
    # after name:
    m = re.search(r'\bname\s*[:=-]\s*([^\n,]+)', text, re.I)
    return m.group(1).strip() if m else None

def extract_owner(text: str):
    # by Alice / owner Bob / for Charlie
    m = re.search(r'\b(?:by|owner|for)\s*[:=-]?\s*([A-Z][\w.&-]*(?:\s+[A-Z][\w.&-]*){0,3})', text, re.I)
    if m:
        return m.group(1).strip()
    # fallback: first capitalized word not at start
    m = re.search(r'(?<!^)\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2})\b', text)
    return m.group(1).strip() if m else None

def extract_location(text: str):
    for rx in (URL_RE, BUCKET_RE, PATH_RE):
        m = rx.search(text)
        if m:
            return m.group(1) if m.groups() else m.group(0)
    # after location:
    m = re.search(r'\blocation\s*[:=-]\s*([^\n,]+)', text, re.I)
    return m.group(1).strip() if m else None

def extract_add_media_slots(text: str):
    return {
        "name": extract_name(text),
        "owner": extract_owner(text),
        "location": extract_location(text),
    }


def fill_slots_for_intent(intent: str, user_text: str):
    if intent == "add_media":
        return extract_add_media_slots(user_text)
    # ...other intents...
    return {}

def missing_slots(intent: str, slots: dict):
    req = ROUTES[intent]["required"]
    return [k for k in req if not slots.get(k)]

# Function to determine intent from response text
def get_intent_from_response(response_text):
    # Check if this looks like an add_media request
    add_media_keywords = ["add", "create", "new", "insert", "include"]
    
    # Convert to lowercase for comparison
    response_lower = response_text.lower()
    
    # Check if user input contains add_media keywords
    for keyword in add_media_keywords:
        if keyword in response_lower:
            return "add_media"
    
    # Default to chitchat for other responses
    return "chitchat"

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
