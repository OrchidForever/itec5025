-- Create database schema for horror story data
CREATE SCHEMA IF NOT EXISTS stories;

-- Story metadata table
CREATE TABLE stories.story_metadata (
    id SERIAL PRIMARY KEY,
    genre VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    max_success_points INTEGER NOT NULL,
    min_success_points INTEGER NOT NULL,
    genre_id INTEGER NOT NULL
);

-- Story texts table
CREATE TABLE stories.story_texts (
    id SERIAL PRIMARY KEY,
    story_id INTEGER REFERENCES stories.story_metadata(id),
    text_type VARCHAR(50) NOT NULL,
    content TEXT NOT NULL
);

-- Choice mappings table
CREATE TABLE stories.choice_mappings (
    id SERIAL PRIMARY KEY,
    story_id INTEGER REFERENCES stories.story_metadata(id),
    choice_set VARCHAR(50) NOT NULL,
    choice_text VARCHAR(100) NOT NULL,
    choice_id INTEGER NOT NULL
);

-- Training data contexts
CREATE TABLE stories.training_contexts (
    id SERIAL PRIMARY KEY,
    story_id INTEGER REFERENCES stories.story_metadata(id),
    context_text TEXT NOT NULL
);

-- Training choices
CREATE TABLE stories.training_choices (
    id SERIAL PRIMARY KEY,
    context_id INTEGER REFERENCES stories.training_contexts(id),
    choice_text VARCHAR(100) NOT NULL,
    choice_id INTEGER NOT NULL
);

-- Training outcomes
CREATE TABLE stories.training_outcomes (
    id SERIAL PRIMARY KEY,
    context_id INTEGER REFERENCES stories.training_contexts(id),
    choice_id INTEGER NOT NULL,
    points INTEGER NOT NULL,
    outcome_text TEXT NOT NULL
);

-- Constants table for point values
CREATE TABLE stories.point_constants (
    constant_name VARCHAR(50) PRIMARY KEY,
    value INTEGER NOT NULL
);

-- Insert point constants
INSERT INTO
    stories.point_constants (constant_name, value)
VALUES
    ('MAJOR_DISCOVERY_POINTS', 2),
    ('MINOR_DISCOVERY_POINTS', 1),
    ('NEGATIVE_DISCOVERY_POINTS', -1);

-- Insert story metadata
INSERT INTO
    stories.story_metadata (
        genre,
        title,
        description,
        max_success_points,
        min_success_points,
        genre_id
    )
VALUES
    (
        'horror',
        'Black Hollow Academy',
        'A chilling tale set in a haunted academy where dark secrets lurk in the shadows.',
        4,
        2,
        0
    );

-- Insert story texts
INSERT INTO
    stories.story_texts (story_id, text_type, content)
VALUES
    (
        1,
        'opening_story',
        'Black Hollow Academy was built in 1812, a sprawling estate of cold stone and older secrets. The new scholarship students arrived just before winter—seven of them, handpicked. The eighth bed in the dormitory is always made, though no one remembers doing it...'
    ),
    (
        1,
        'opening_choice_text',
        'You hear whispers in the hallways, shadows moving where there should be none. The headmaster is strict, but there''s something off about him. The other students are friendly, but their eyes seem to hold secrets. Do you want to visit the library or talk to the headmaster? Alternatively, you can gather with the other students to share stories of the strange occurrences.'
    ),
    (
        1,
        'positive_message',
        'The whispers in your head only seem to grow louder, but you feel a sense of determination to uncover the truth.'
    ),
    (
        1,
        'negative_message',
        'Your head is swimming as the voices swell and you''re not sure how much more of this school you can take.'
    ),
    (
        1,
        'max_success_text',
        'You have successfully uncovered the dark secrets of Black Hollow Academy. The feeling of dread lingers, but you have the knowledge to protect yourself and others.'
    ),
    (
        1,
        'min_success_text',
        'You have discovered some unsettling truths about Black Hollow Academy. You know there is more to discover but you need to be careful. Next year.'
    ),
    (
        1,
        'failure_text',
        'You have failed to uncover the secrets of Black Hollow Academy. The whispers grow louder, and you feel a sense of dread as you leave the academy behind.'
    ),
    (
        1,
        'end_story_text',
        'The end of the year is wrapping up. The whispers in your head are louder than ever, but you feel a sense of accomplishment for surviving a year at Black Hollow Academy. Some were not as accomplished as you.'
    );

-- Insert choice mappings
INSERT INTO
    stories.choice_mappings (story_id, choice_set, choice_text, choice_id)
VALUES
    (1, 'valid_choices_1', 'library', 0),
    (1, 'valid_choices_1', 'headmaster', 1),
    (1, 'valid_choices_1', 'students', 2),
    (1, 'valid_choices_2', 'explore', 0),
    (1, 'valid_choices_2', 'confront', 1),
    (1, 'valid_choices_2', 'leave', 2);

-- Insert training contexts
INSERT INTO
    stories.training_contexts (story_id, context_text)
VALUES
    (
        1,
        'You enter the library, the smell of old books fills the air. You find a dusty tome that seems to call to you...'
    ),
    (
        1,
        'You try to meet with the headmaster but he''s not there... You feel a sense of unease as you realize that he might be hiding something.'
    );

-- Insert training choices
INSERT INTO
    stories.training_choices (context_id, choice_text, choice_id)
VALUES
    (1, 'read', 0),
    (1, 'put back', 1),
    (2, 'pick', 0),
    (2, 'leave', 1);

-- Insert training outcomes
INSERT INTO
    stories.training_outcomes (context_id, choice_id, points, outcome_text)
VALUES
    (
        1,
        0,
        1,
        'As you read, the words seem to shift and change, revealing a dark secret about the academy...'
    ),
    (
        1,
        1,
        -1,
        'You decide not to disturb the tome, but you can''t shake the feeling that it holds important information...'
    ),
    (
        2,
        0,
        2,
        'You manage to pick the lock and enter the office. The walls are lined with portraits of previous headmasters...'
    ),
    (
        2,
        1,
        -1,
        'You decide to leave the office alone, but you can''t shake the feeling that the headmaster is hiding something important...'
    );

-- Adventure story data for the chatbot system
-- Based on the horror.sql schema structure
-- Insert adventure story metadata
INSERT INTO
    stories.story_metadata (
        genre,
        title,
        description,
        max_success_points,
        min_success_points,
        genre_id
    )
VALUES
    (
        'adventure',
        'The Lost Temple of Valdoria',
        'An epic quest to discover an ancient temple filled with treasures and deadly traps in the heart of the Amazon rainforest.',
        4,
        2,
        1
    );

-- Insert story texts for adventure
INSERT INTO
    stories.story_texts (story_id, text_type, content)
VALUES
    (
        2,
        'opening_story',
        'Deep in the Amazon rainforest lies the Lost Temple of Valdoria, a legendary structure said to contain the Golden Compass of eternal navigation. You are an archaeologist who has finally decoded the ancient map. Standing at the jungle''s edge with your backpack and machete, you see three possible paths through the dense vegetation...'
    ),
    (
        2,
        'opening_choice_text',
        'The jungle is alive with sounds of exotic birds and rustling leaves. You notice three distinct paths: a well-worn trail that looks safer but longer, a narrow path through thick vines that seems more direct, and a rocky path along a stream that might lead to higher ground for better navigation. Which path do you choose to reach the temple?'
    ),
    (
        2,
        'positive_message',
        'Your adventurer''s instincts are sharp and you feel confident about your progress toward the ancient temple.'
    ),
    (
        2,
        'negative_message',
        'The jungle seems to be working against you, and you''re starting to question if you''re on the right path.'
    ),
    (
        2,
        'max_success_text',
        'You have successfully navigated the temple''s trials and claimed the Golden Compass of Valdoria! Your name will be remembered among the greatest explorers.'
    ),
    (
        2,
        'min_success_text',
        'You have reached the temple and discovered some of its secrets, though the greatest treasures remain hidden for future expeditions.'
    ),
    (
        2,
        'failure_text',
        'The jungle has claimed another explorer. You must retreat empty-handed, but with valuable knowledge for your next attempt.'
    ),
    (
        2,
        'end_story_text',
        'As you emerge from the jungle, whether victorious or defeated, you carry with you the memories of an incredible adventure that will fuel your dreams of future expeditions.'
    );

-- Insert choice mappings for adventure
INSERT INTO
    stories.choice_mappings (story_id, choice_set, choice_text, choice_id)
VALUES
    (2, 'valid_choices_1', 'trail', 0),
    (2, 'valid_choices_1', 'vines', 1),
    (2, 'valid_choices_1', 'stream', 2),
    (2, 'valid_choices_2', 'torch', 0),
    (2, 'valid_choices_2', 'rope', 1),
    (2, 'valid_choices_2', 'compass', 2);

-- Insert training contexts for adventure
INSERT INTO
    stories.training_contexts (story_id, context_text)
VALUES
    (
        2,
        'You reach a massive stone door covered in ancient symbols. There are three keyholes shaped like different animals: a jaguar, an eagle, and a serpent. You have found three corresponding keys during your journey...'
    ),
    (
        2,
        'Inside the temple, you discover a chamber with a deep pit. Ancient rope bridges span across, but they look weathered. You can see golden artifacts glinting on the other side...'
    ),
    (
        2,
        'You encounter a rushing underground river blocking your path. You notice a sturdy vine hanging from the ceiling and some loose stones that could be used as stepping stones...'
    ),
    (
        2,
        'In the temple''s heart, you find a pedestal with the Golden Compass, but it''s surrounded by pressure plates. Ancient murals on the walls seem to hint at the correct sequence...'
    );

-- Insert training choices for adventure
INSERT INTO
    stories.training_choices (context_id, choice_text, choice_id)
VALUES
    (3, 'jaguar first', 0),
    (3, 'eagle first', 1),
    (3, 'serpent first', 2),
    (4, 'test bridge', 0),
    (4, 'find another way', 1),
    (4, 'use rope', 2),
    (5, 'swing vine', 0),
    (5, 'stone hop', 1),
    (5, 'wade across', 2),
    (6, 'study murals', 0),
    (6, 'step randomly', 1),
    (6, 'use tools', 2);

-- Insert training outcomes for adventure
INSERT INTO
    stories.training_outcomes (context_id, choice_id, points, outcome_text)
VALUES
    (
        3,
        0,
        2,
        'The jaguar key opens the door with a satisfying click. Ancient wisdom favors the hunter''s approach.'
    ),
    (
        3,
        1,
        1,
        'The eagle key works, but you hear ominous grinding sounds. You''ve chosen a valid but dangerous path.'
    ),
    (
        3,
        2,
        -1,
        'The serpent key triggers a trap! Darts fly from the walls, forcing you to retreat and try again.'
    ),
    (
        4,
        0,
        1,
        'You carefully test the bridge and find it sturdy enough. Your cautious approach pays off.'
    ),
    (
        4,
        1,
        -1,
        'While searching for another route, you waste precious time and daylight begins to fade.'
    ),
    (
        4,
        2,
        2,
        'Using your rope to secure a crossing proves brilliant - you discover a hidden cache of gems!'
    ),
    (
        5,
        0,
        2,
        'Your vine swing is perfect! You land gracefully and notice a secret passage behind the waterfall.'
    ),
    (
        5,
        1,
        1,
        'You successfully hop across the stones, though you slip once and get soaked.'
    ),
    (
        5,
        2,
        -1,
        'The current is stronger than expected and you nearly lose your equipment while struggling across.'
    ),
    (
        6,
        0,
        2,
        'The murals reveal the ancient pattern! You step confidently and claim the Golden Compass.'
    ),
    (
        6,
        1,
        -1,
        'Your random steps trigger multiple traps. You escape but the compass remains unreachable.'
    ),
    (
        6,
        2,
        1,
        'Your modern tools help you partially decode the sequence, allowing you to grab some treasure.'
    );

-- Insert noir detective story metadata
INSERT INTO
    stories.story_metadata (
        genre,
        title,
        description,
        max_success_points,
        min_success_points,
        genre_id
    )
VALUES
    (
        'noir',
        'The Midnight Dame',
        'A gritty detective story set in 1940s rain-soaked streets where shadows hide deadly secrets and every dame has a story to tell.',
        4,
        2,
        2
    );

-- Insert story texts for noir detective
INSERT INTO
    stories.story_texts (story_id, text_type, content)
VALUES
    (
        3,
        'opening_story',
        'The rain hammered the city like bullets on a tin roof. It was past midnight when she walked into my office—red dress, trouble in her eyes, and enough curves to make a man forget his own name. "Detective," she said, voice like honey over broken glass, "I need your help. Someone wants me dead, and I think I know who." The neon sign outside my window flickered like a dying heartbeat...'
    ),
    (
        3,
        'opening_choice_text',
        'The dame sits across from your desk, cigarette smoke curling between you like secrets. She claims her wealthy husband wants her eliminated for the insurance money, but something doesn''t add up. You notice her nervous glances toward the window and the way she clutches her purse. Do you press her for more details about her husband, examine the threatening letters she brought, or follow your gut instinct that she''s hiding something?'
    ),
    (
        3,
        'positive_message',
        'Your detective instincts are sharp tonight. The pieces of this puzzle are starting to come together in the shadows.'
    ),
    (
        3,
        'negative_message',
        'The case grows murkier by the hour. Every lead seems to dissolve like smoke in the rain-soaked streets.'
    ),
    (
        3,
        'max_success_text',
        'You''ve cracked the case wide open. The truth was uglier than the city''s underbelly, but justice will be served. The dame''s secrets are laid bare under the harsh light of evidence.'
    ),
    (
        3,
        'min_success_text',
        'You''ve solved part of the mystery, but some shadows in this city run too deep. The dame disappears into the night, leaving you with more questions than answers.'
    ),
    (
        3,
        'failure_text',
        'The case went cold faster than a corpse in the morgue. The dame played you like a fiddle, and now she''s vanished into the neon-lit maze of the city.'
    ),
    (
        3,
        'end_story_text',
        'Dawn breaks over the city like a hangover. Whether you solved the case or got played, the streets keep their secrets. There''s always another case, another dame, another shadow waiting in tomorrow''s rain.'
    );

-- Insert choice mappings for noir detective
INSERT INTO
    stories.choice_mappings (story_id, choice_set, choice_text, choice_id)
VALUES
    (3, 'valid_choices_1', 'husband', 0),
    (3, 'valid_choices_1', 'letters', 1),
    (3, 'valid_choices_1', 'instinct', 2),
    (3, 'valid_choices_2', 'follow', 0),
    (3, 'valid_choices_2', 'confront', 1),
    (3, 'valid_choices_2', 'investigate', 2);

-- Insert training contexts for noir detective
INSERT INTO
    stories.training_contexts (story_id, context_text)
VALUES
    (
        3,
        'You tail the dame to a smoky jazz club downtown. Through the haze, you see her slip an envelope to a shadowy figure at the bar. The bartender pretends not to notice, but his eyes follow every move...'
    ),
    (
        3,
        'Back at the office, you examine the threatening letters under your desk lamp. The paper is expensive, the handwriting educated, but something about the ink smudges suggests they were written in haste—or fear...'
    ),
    (
        3,
        'You decide to pay the husband a visit at his mansion uptown. The butler answers the door with suspicious eyes, and you hear raised voices from inside. A woman''s scream pierces the night air...'
    ),
    (
        3,
        'At the police station, your contact in the department slides a file across the desk. "Three wives," he whispers, "all died in accidents. All heavily insured. And all looked just like your dame..."'
    );

-- Insert training choices for noir detective
INSERT INTO
    stories.training_choices (context_id, choice_text, choice_id)
VALUES
    (7, 'approach figure', 0),
    (7, 'question bartender', 1),
    (7, 'wait and watch', 2),
    (8, 'analyze handwriting', 0),
    (8, 'check paper source', 1),
    (8, 'test for fingerprints', 2),
    (9, 'rush inside', 0),
    (9, 'question butler', 1),
    (9, 'circle the house', 2),
    (10, 'demand more files', 0),
    (10, 'investigate deaths', 1),
    (10, 'warn the dame', 2);

-- Insert training outcomes for noir detective
INSERT INTO
    stories.training_outcomes (context_id, choice_id, points, outcome_text)
VALUES
    (
        7,
        0,
        2,
        'The shadowy figure reveals himself as a private investigator hired by the dame''s husband. The plot thickens like day-old coffee.'
    ),
    (
        7,
        1,
        1,
        'The bartender admits to seeing regular exchanges but claims ignorance. His nervous twitch suggests otherwise.'
    ),
    (
        7,
        2,
        -1,
        'Your patience pays off with nothing but a cold trail. The dame and her contact vanish into the night like ghosts.'
    ),
    (
        8,
        0,
        1,
        'The handwriting analysis reveals an educated hand, but the pressure suggests extreme stress or fear.'
    ),
    (
        8,
        1,
        2,
        'The expensive paper comes from an exclusive stationery shop. Only three customers bought this type recently.'
    ),
    (
        8,
        2,
        -1,
        'The letters have been handled too much. Any useful fingerprints are long gone, leaving you with nothing.'
    ),
    (
        9,
        0,
        -1,
        'You burst in to find a radio drama playing. The "scream" was just sound effects, but now you''ve blown your cover.'
    ),
    (
        9,
        1,
        1,
        'The butler''s nervous demeanor and evasive answers tell you more than his words. Something''s rotten in this mansion.'
    ),
    (
        9,
        2,
        2,
        'Your surveillance reveals a secret entrance and suspicious activity. The husband is definitely hiding something big.'
    ),
    (
        10,
        0,
        2,
        'The additional files reveal a pattern of murders disguised as accidents. You''ve uncovered a serial killer.'
    ),
    (
        10,
        1,
        1,
        'Your investigation into the deaths reveals inconsistencies in the official reports, but the trail is getting dangerous.'
    ),
    (
        10,
        2,
        -1,
        'You try to warn the dame, but she''s vanished. Either she''s the next victim, or she''s playing a deeper game.'
    );

-- Create indexes for better performance
CREATE INDEX idx_story_texts_story_id ON stories.story_texts(story_id);

CREATE INDEX idx_choice_mappings_story_id ON stories.choice_mappings(story_id);

CREATE INDEX idx_training_contexts_story_id ON stories.training_contexts(story_id);

CREATE INDEX idx_training_choices_context_id ON stories.training_choices(context_id);

CREATE INDEX idx_training_outcomes_context_id ON stories.training_outcomes(context_id);