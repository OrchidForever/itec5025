CREATE TABLE IF NOT EXISTS media (
    id SERIAL PRIMARY KEY,
    -- Unique identifier for each media item
    title VARCHAR(255) NOT NULL,
    -- Title of the media
    format VARCHAR(50) NOT NULL,
    -- Format (e.g., Book, DVD, Audiobook)
    owner VARCHAR(50) NOT NULL,
    -- Owner of the media
    location VARCHAR(255),
    -- Location where the media is stored
    status VARCHAR(50) NOT NULL -- Status (e.g., Available, Lost)
);

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Dune',
        'Book',
        'Tom',
        'Living room shelf',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Animal Crossing',
        'Switch Game',
        'Brenna',
        'Switch game case',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'The Last of Us Part II',
        'PS5 Game',
        'Tom',
        'Media cabinet',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Harry Potter and the Sorcerer''s Stone',
        'Audiobook',
        'Brenna',
        'Audible',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Blade Runner 2049',
        'DVD',
        'Tom',
        'TV console drawer',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Cyberpunk 2077',
        'Steam Game',
        'Tom',
        'Steam library',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Stardew Valley',
        'Switch Game',
        'Brenna',
        'Switch game case',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Pride and Prejudice',
        'Book',
        'Brenna',
        'Bedroom bookshelf',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'The Matrix',
        'DVD',
        'Tom',
        'DVD binder',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Dune',
        'Audiobook',
        'Brenna',
        'Audible',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Red Dead Redemption 2',
        'PS5 Game',
        'Tom',
        'Game shelf',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Educated',
        'Audiobook',
        'Brenna',
        'Audible',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'The Hobbit',
        'Book',
        'Tom',
        'Hallway bookshelf',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Interstellar',
        'DVD',
        'Tom',
        'DVD binder',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Becoming',
        'Audiobook',
        'Brenna',
        'Audible',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Hades',
        'Steam Game',
        'Tom',
        'Steam library',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Gone Girl',
        'Book',
        'Brenna',
        'Unknown',
        'Lost'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Celeste',
        'Switch Game',
        'Shared',
        'Switch digital library',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'The Witcher 3',
        'Steam Game',
        'Shared',
        'Steam shared library',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'The Great Gatsby',
        'Book',
        'Tom',
        'Unknown',
        'Lost'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Inside Out',
        'DVD',
        'Brenna',
        'Kids movie binder',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'The Subtle Art of Not Giving a F*ck',
        'Audiobook',
        'Tom',
        'Audible',
        'Available'
    );

INSERT INTO
    media (title, format, owner, location, status)
VALUES
    (
        'Mario Kart',
        'Switch Game',
        'Shared',
        'Switch game case',
        'Available'
    );