import tensorflow as tf	
import numpy as np

# Create a constant tensor
hello = tf.constant('Hello, Chatbot!')

print("TensorFlow version:", tf.__version__)
print(hello.numpy().decode('utf-8'))  # Use .numpy() to get the value

# Use the dataset builder from data.prepare_tf_data
try:
    from data.prepare_tf_data import build_dataset
except Exception:
    from prepare_tf_data import build_dataset


def build_simple_classifier(vocab_size: int, seq_len: int, num_genres: int, num_classes: int) -> tf.keras.Model:
    """Build a small classifier that takes (text_tokens, genre_id) -> choice logits."""
    text_input = tf.keras.Input(shape=(seq_len,), dtype=tf.int32, name="text")
    genre_input = tf.keras.Input(shape=(), dtype=tf.int32, name="genre")

    x = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=64, mask_zero=False)(text_input)
    x = tf.keras.layers.GlobalAveragePooling1D()(x)

    g = tf.keras.layers.Embedding(input_dim=num_genres, output_dim=8)(genre_input)
    g = tf.keras.layers.Flatten()(g)

    h = tf.keras.layers.Concatenate()([x, g])
    h = tf.keras.layers.Dense(64, activation="relu")(h)
    out = tf.keras.layers.Dense(num_classes, activation="softmax")(h)

    model = tf.keras.Model([text_input, genre_input], out)
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model


if __name__ == "__main__":
    try:
        ds, vectorizer, num_classes, raw_examples, num_genres = build_dataset(batch_size=4, seq_len=64)
        print("Dataset ready. num_classes:", num_classes, "num_genres:", num_genres)

        # inspect
        for (xb, gb), yb in ds.take(1):
            print("x batch shape:", xb.shape, "genre shape:", gb.shape, "y shape:", yb.shape)
            print("y sample:", yb.numpy())

        # Build and train a tiny classifier if there is more than 1 example
        if tf.data.experimental.cardinality(ds).numpy() > 0:
            vocab_size = len(vectorizer.get_vocabulary())
            seq_len = xb.shape[1]
            model = build_simple_classifier(vocab_size=vocab_size, seq_len=seq_len, num_genres=num_genres, num_classes=num_classes)
            print(model.summary())

            # Train briefly (safe: only 5 epochs)
            model.fit(ds, epochs=5)

            # Demo inference on first raw example
            first = raw_examples[0]
            ctx = first.get("context", "")
            # Use genre_id from the example if present; fall back to 0
            genre_id = int(first.get("genre_id", 0))
            x_vec = vectorizer([ctx])
            pred = model.predict([x_vec, np.array([genre_id])])
            choice_id = int(pred.argmax(axis=-1)[0])

            print("Predicted choice_id:", choice_id)
            # Find matching outcome and print its text
            outcomes = first.get("outcomes", [])
            matched = None
            for o in outcomes:
                if int(o.get("choice_id", -1)) == choice_id:
                    matched = o
                    break
            if matched:
                print("Generated outcome text:\n", matched.get("text", ""))
            else:
                print("No matching outcome text found for predicted choice.")

    except Exception as e:
        print("Could not build/train dataset/model:", e)

print("Session ended.")