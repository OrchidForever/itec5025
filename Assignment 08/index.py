import tensorflow as tf
import csv

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
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == 'quit':
            break
        vec_input = vectorizer([user_input])
        pred = model.predict(vec_input)
        response_index = tf.argmax(pred, axis=1).numpy()[0]
        print(f"[DEBUG] Predicted class index: {response_index}")

        print("Bot:", index_to_response[response_index])

chatbot()
