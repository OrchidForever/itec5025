import os
import tensorflow as tf
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from utils.clean_data import preprocess_text
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import TextVectorization, Input
from tensorflow.keras.models import Model
import csv

print("TensorFlow version:", tf.__version__)
print("Hello, Chatbot!") 

output_path = "data/processed_convo_data.csv"

def clean_data_setup():
    # Load the CSV data
    data_path = "data/convo_data.csv"
    data = pd.read_csv(data_path, quotechar='"', escapechar='\\')

    # Normalize both columns of data
    print("Preprocessing user_input data...")
    data["user_input_clean"] = data["user_input"].apply(preprocess_text)
    print("Preprocessing bot_response data...")
    data["bot_response_clean"] = data["bot_response"].apply(preprocess_text)

    # Drop any rows with missing bot responses
    data = data.dropna(subset=["bot_response_clean"])

   # Create response labels
    responses_set = sorted(set(data["bot_response_clean"]))
    response_to_index = {resp: i for i, resp in enumerate(responses_set)}
    index_to_response = {i: resp for resp, i in response_to_index.items()}
    y = [response_to_index[resp] for resp in data["bot_response_clean"]]

    # Train/test split
    X_train_texts, X_test_texts, y_train, y_test = train_test_split(data["user_input_clean"], y, test_size=0.2)

    # Setup TextVectorization layer and adapt to training texts
    max_vocab_size = 10000
    max_len = 25

    vectorizer = tf.keras.layers.TextVectorization(
        max_tokens=max_vocab_size,
        output_mode='int',
        output_sequence_length=max_len
    )

    vectorizer.adapt(X_train_texts)

    # Vectorize texts
    X_train = vectorizer(tf.constant(X_train_texts))
    X_test = vectorizer(tf.constant(X_test_texts))

    # Convert labels to tensors
    y_train = tf.convert_to_tensor(y_train)
    y_test = tf.convert_to_tensor(y_test)

    # Build and compile model
    # model = tf.keras.Sequential([
    #     tf.keras.layers.Embedding(input_dim=max_vocab_size, output_dim=64, input_length=max_len),
    #     tf.keras.layers.GlobalAveragePooling1D(),
    #     tf.keras.layers.Dense(64, activation='relu'),
    #     tf.keras.layers.Dense(len(responses_set), activation='softmax')
    # ])

    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=max_vocab_size, output_dim=128, input_length=max_len),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(len(responses_set), activation='softmax')
    ])

    # model = tf.keras.Sequential([
    #     tf.keras.layers.Embedding(input_dim=max_vocab_size, output_dim=128, input_length=max_len),
    #     tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True)),
    #     tf.keras.layers.Dropout(0.5),  # Dropout to prevent overfitting
    #     tf.keras.layers.GlobalAveragePooling1D(),  # You can replace the last LSTM with a pooling layer
    #     tf.keras.layers.Dense(64, activation='relu'),
    #     tf.keras.layers.Dense(len(responses_set), activation='softmax')
    # ])

    # accuracy: 0.0237 - loss: 4.9634 - val_accuracy: 0.0000e+00 - val_loss: 7.6289
    # model = tf.keras.Sequential([
    #     tf.keras.layers.Embedding(input_dim=max_vocab_size, output_dim=64, input_length=max_len),
    #     tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),  # Smaller LSTM units
    #     tf.keras.layers.Dropout(0.5),  # Dropout to prevent overfitting
    #     tf.keras.layers.Dense(len(responses_set), activation='softmax')  # Output layer directly
    # ])

    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train
    model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

    # Save model and vectorizer
    model.save("data/chatbot_model.keras")

    vectorizer_path = "data/vectorizer.keras"
    input_layer = Input(shape=(1,), dtype=tf.string)
    output_layer = vectorizer(input_layer)
    vectorizer_model = Model(inputs=input_layer, outputs=output_layer)

    vectorizer_model.save(vectorizer_path)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "response"])
        for idx, resp in index_to_response.items():
            writer.writerow([idx, resp])


    print(f"Processed data saved to {output_path}")

# Check if output file exists to avoid reprocessing

if os.path.exists(output_path):
    print(f"Output file already exists, skipping processing: {output_path}")
else:
    clean_data_setup()