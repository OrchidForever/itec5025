import re

def preprocess_text(text):
    """Basic text preprocessing: lowercase, remove special characters, normalize spaces."""
    text = str(text).strip()
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s']", "", text)
    text = re.sub(r"\s+", " ", text)
    print(f"Preprocessed text: {text}")
    return text
