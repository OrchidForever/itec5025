"""Generate an SQL file to create the intents table from in-memory dataset structure.

Usage:
    python make_intents_sql.py > create_intents_table.sql
    python make_intents_sql.py out.sql  # write to file

This script will inspect `Assignment 06/data/base_json.py` HORROR_STORY_TF and
produce INSERT statements for each training example as well as a CREATE TABLE
statement. It writes to stdout by default or to a file when provided.
"""
import json
from pathlib import Path
import sys

try:
    from data.base_json import HORROR_STORY_TF
except Exception:
    from base_json import HORROR_STORY_TF


CREATE = '''CREATE TABLE IF NOT EXISTS intents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_id INTEGER NOT NULL,
    context TEXT NOT NULL,
    choices TEXT,
    choice_ids TEXT,
    outcomes TEXT,
    label INTEGER,
    points INTEGER,
    created_at TEXT DEFAULT (datetime('now'))
);
'''


def generate_sql_text(horror_story_tf: dict) -> str:
    """Build the full SQL text (CREATE + INSERTs) and return it as a string."""
    parts = [CREATE]
    examples = horror_story_tf.get('training_data', [])
    for ex in examples:
        genre = ex.get('genre_id', horror_story_tf.get('metadata', {}).get('genre_id', 0))
        context = ex.get('context', '').replace("'", "''")
        choices = json.dumps(ex.get('choices', []))
        choice_ids = json.dumps(ex.get('choice_ids', []))
        outcomes = json.dumps(ex.get('outcomes', []))
        if ex.get('outcomes'):
            best = max(ex.get('outcomes', []), key=lambda o: o.get('points', 0))
            label = best.get('choice_id', 'NULL')
            points = best.get('points', 'NULL')
        else:
            label = 'NULL'
            points = 'NULL'
        stmt = (
            f"INSERT INTO intents (genre_id, context, choices, choice_ids, outcomes, label, points) "
            f"VALUES ({genre}, '{context}', '{choices}', '{choice_ids}', '{outcomes}', {label}, {points});"
        )
        parts.append(stmt)
    return "\n".join(parts)


if __name__ == '__main__':
    sql_text = generate_sql_text(HORROR_STORY_TF)
    # If a path is provided, write to that file; otherwise print to stdout
    if len(sys.argv) > 1:
        out_path = Path(sys.argv[1])
        out_path.write_text(sql_text, encoding='utf-8')
        print(f"Wrote SQL to {out_path}")
    else:
        print(sql_text)
