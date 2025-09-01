"""Prepare TensorFlow dataset from the HORROR_STORY_TF data structure.

This helper extracts (text, label, genre) pairs from the training_data entries in
`base_json.py`, vectorizes the text with TextVectorization and returns a
batched tf.data.Dataset ready for model training. It also returns the raw
examples and the number of genres so the training script can use them for
template-based generation.
"""
from typing import List, Tuple

import tensorflow as tf

# Try relative import first (when used as package), fallback to direct import
try:
    from .base_json import HORROR_STORY_TF
except Exception:
    from base_json import HORROR_STORY_TF


def _get_label_from_outcomes(outcomes: List[dict]) -> int:
    """Choose the outcome with the highest points as the label.

    Returns the choice_id (int). If outcomes is empty, returns 0.
    """
    if not outcomes:
        return 0
    best = max(outcomes, key=lambda o: o.get("points", 0))
    return int(best.get("choice_id", 0))


def extract_examples() -> Tuple[List[str], List[int], List[int], List[List[dict]]]:
    """Extract (texts, labels, genres, outcomes_list) from training_data.

    Returns:
      texts: list of context strings
      labels: integer class ids (choice_id selected by _get_label_from_outcomes)
      genres: integer genre ids per example (falls back to metadata genre_id)
      outcomes_list: list of the raw outcomes for each example (used for templates)
    """
    examples = HORROR_STORY_TF.get("training_data", [])
    texts: List[str] = []
    labels: List[int] = []
    genres: List[int] = []
    outcomes_list: List[List[dict]] = []

    default_genre = HORROR_STORY_TF.get("metadata", {}).get("genre_id", 0)

    for ex in examples:
        context = ex.get("context", "") or ""
        texts.append(context)
        labels.append(_get_label_from_outcomes(ex.get("outcomes", [])))
        genres.append(int(ex.get("genre_id", default_genre)))
        outcomes_list.append(ex.get("outcomes", []))

    return texts, labels, genres, outcomes_list


def build_text_vectorizer(texts: List[str], max_tokens: int = 20000, seq_len: int = 128) -> tf.keras.layers.TextVectorization:
    """Build and adapt a TextVectorization layer on given texts."""
    vectorizer = tf.keras.layers.TextVectorization(
        max_tokens=max_tokens,
        output_mode="int",
        output_sequence_length=seq_len,
    )
    if texts:
        ds_for_adapt = tf.data.Dataset.from_tensor_slices(texts).batch(32)
        vectorizer.adapt(ds_for_adapt)
    return vectorizer


def build_dataset(batch_size: int = 16, seq_len: int = 128) -> Tuple[tf.data.Dataset, tf.keras.layers.TextVectorization, int, List[dict], int]:
    """Return (dataset, vectorizer, num_classes, raw_examples_outcomes, num_genres).

    Dataset yields ((vectorized_text, genre_id), label) where vectorized_text is an
    int tensor of shape (batch, seq_len) and label is an int32 tensor.
    """
    texts, labels, genres, outcomes_list = extract_examples()
    examples_raw = HORROR_STORY_TF.get("training_data", [])

    if len(texts) == 0:
        raise ValueError("No training_data found in HORROR_STORY_TF")

    vectorizer = build_text_vectorizer(texts, seq_len=seq_len)

    # Build dataset from (text, genre, label)
    ds = tf.data.Dataset.from_tensor_slices((texts, genres, labels))

    def _vectorize(text):
        vec = vectorizer(tf.expand_dims(text, axis=0))
        vec = tf.squeeze(vec, axis=0)
        return vec

    def map_fn(text, genre, label):
        vec = _vectorize(text)
        return (vec, tf.cast(genre, tf.int32)), tf.cast(label, tf.int32)

    ds = ds.shuffle(buffer_size=max(1, len(texts))).map(map_fn, num_parallel_calls=tf.data.AUTOTUNE)
    ds = ds.batch(batch_size).prefetch(tf.data.AUTOTUNE)

    num_classes = int(max(labels)) + 1 if labels else 1
    num_genres = int(max(genres)) + 1 if genres else 1

    return ds, vectorizer, num_classes, examples_raw, num_genres


if __name__ == "__main__":
    ds, vect, ncls, examples, ngenres = build_dataset(batch_size=4, seq_len=64)
    print("Built dataset. num_classes=", ncls, "num_genres=", ngenres)
    for (xb, gb), yb in ds.take(1):
        print("x batch shape:", xb.shape)
        print("genre batch shape:", gb.shape)
        print("y batch shape:", yb.shape)
        print("Sample y:", yb.numpy())
