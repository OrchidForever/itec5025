import re
from routes.index import ROUTES
import spacy

PROMPTS = {
    ("add_media", "name"): "What's the media name? (you can put it in quotes)",
    ("add_media", "owner"): "Who is the owner?",
    ("add_media", "location"): "Where is it located? (URL, file path, or bucket URI)",
    ("add_media", "format"): "What is the media format?",
    ("search_media", "name"): "Which media name are you looking for?",
    ("search_media", "owner"): "Which owner are you interested in?",
    ("search_media", "location"): "Which location are you interested in?",
    ("search_media", "format"): "Which format are you interested in?",
    ("update_media_status", "name"): "Which media item do you want to update?",
    ("update_media_status", "status"): "What is the new status?"
}

add_media_keywords = ["add", "create", "new", "insert", "include", "added"]
search_media_keywords = ["search", "find", "look for", "get", "retrieve", "where"]
update_media_keywords = ["update", "change", "modify", "set"]

INTENT_PATTERNS = {
    'add_media': {
        'keywords': add_media_keywords,
        'slots': ["name", "owner", "location", "format"],
        'pos': ["PROPN", "NOUN", "VERB", "LOCATION"],
        'entities': ["PERSON", "ORG", "GPE", "LOC", "PRODUCT"]
    },
    'search_media': {
        'keywords': search_media_keywords,
        'slots': ["name", "owner", "location", "format"],
        'pos': ["PROPN", "NOUN", "VERB", "LOCATION", "WP", "WRB"],
        'entities': ["PERSON", "ORG", "GPE", "LOC", "PRODUCT"]
    },
    'update_media_status': {
        'keywords': update_media_keywords,
        'slots': ["name", "status"],
        'pos': ["PROPN", "NOUN", "VERB"],
        'entities': ["PERSON", "ORG", "GPE", "LOC", "PRODUCT", "STATUS"]
    }
}

nlp = spacy.load("en_core_web_sm")

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

def extract_format(text: str):
    m = re.search(r'\bformat\s*[:=-]\s*([^\n,]+)', text, re.I)
    return m.group(1).strip() if m else None

def extract_add_media_slots(text: str):
    return {
        "name": extract_name(text),
        "owner": extract_owner(text),
        "location": extract_location(text),
        "format": extract_format(text),
    }

def extract_search_media_slots(text: str):
    return {
        "name": extract_name(text),
        "owner": extract_owner(text),
        "location": extract_location(text),
        "format": extract_format(text),
    }

def extract_update_media_status_slots(text: str):
    return {
        "name": extract_name(text),
        "status": re.search(r'\b(status|state)\s*[:=-]?\s*([a-zA-Z]+)', text, re.I).group(2) if re.search(r'\b(status|state)\s*[:=-]?\s*([a-zA-Z]+)', text, re.I) else None,
    }


def fill_slots_for_intent(intent: str, user_text: str):
    if intent == "add_media":
        return extract_add_media_slots(user_text)
    elif intent == "search_media":
        return extract_search_media_slots(user_text)
    elif intent == "update_media_status":
        return extract_update_media_status_slots(user_text)
    return {}

def missing_slots(intent: str, slots: dict):
    req = ROUTES[intent]["required"]
    return [k for k in req if not slots.get(k)]

# Function to determine intent from response text
# def get_intent_from_response(response_text):
#     # Check if this looks like an add_media request
#     add_media_keywords = ["add", "create", "new", "insert", "include"]

#     search_media_keywords = ["search", "find", "look for", "get", "retrieve"]
    
#     update_media_keywords = ["update", "change", "modify", "set"]
    
#     # Convert to lowercase for comparison
#     response_lower = response_text.lower()
    
#     # Check if user input contains add_media keywords
#     for keyword in add_media_keywords:
#         if keyword in response_lower:
#             return "add_media"

#     for keyword in search_media_keywords:
#         if keyword in response_lower:
#             return "search_media"
    
#     for keyword in update_media_keywords:
#         if keyword in response_lower:
#             return "update_media_status"

#     # Default to chitchat for other responses
#     return "chitchat"


def get_intent_from_response(response_text):
    doc = nlp(response_text.lower())
    scores = {}

    for intent, patterns in INTENT_PATTERNS.items():
        score = 0
        
        # Check for entities
        if 'entities' in patterns:
            for ent in doc.ents:
                if ent.label_ in patterns['entities']:
                    score += 2
        
        # Check for keywords
        if 'keywords' in patterns:
            for token in doc:
                if token.lemma_ in patterns['keywords']:
                    score += 1
        
        # Check POS tags
        if 'pos' in patterns:
            for token in doc:
                if token.pos_ in patterns['pos']:
                    score += 1
        
        scores[intent] = score

    print(f"The scores: {scores}")
    # Return the intent with highest score, or 'unknown' if no clear match
    if scores:
        max_score = max(scores.values())
        if max_score > 0:
            return max(scores, key=scores.get)
    
    return 'chitchat'
