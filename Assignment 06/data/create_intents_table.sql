CREATE TABLE IF NOT EXISTS intents (
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

INSERT INTO
    intents (
        genre_id,
        context,
        choices,
        choice_ids,
        outcomes,
        label,
        points
    )
VALUES
    (
        0,
        'You enter the library, the smell of old books fills the air. You find a dusty tome that seems to call to you...',
        '["read", "put back"]',
        '[0, 1]',
        '[{"choice_id": 0, "points": 1, "text": "As you read, the words seem to shift and change, revealing a dark secret about the academy..."}, {"choice_id": 1, "points": -1, "text": "You decide not to disturb the tome, but you can not shake the feeling that it holds important information..."}]',
        0,
        1
    );

INSERT INTO
    intents (
        genre_id,
        context,
        choices,
        choice_ids,
        outcomes,
        label,
        points
    )
VALUES
    (
        0,
        'You try to meet with the headmaster but he''s not there... You feel a sense of unease as you realize that he might be hiding something.',
        '["pick", "leave"]',
        '[0, 1]',
        '[{"choice_id": 0, "points": 2, "text": "You manage to pick the lock and enter the office. The walls are lined with portraits of previous headmasters..."}, {"choice_id": 1, "points": -1, "text": "You decide to leave the office alone, but you can not shake the feeling that the headmaster is hiding something important..."}]',
        0,
        2
    );