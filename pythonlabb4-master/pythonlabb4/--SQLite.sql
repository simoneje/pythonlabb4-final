-- SQLite

create table users (
    username VARCHAR(32) UNIQUE,
    password VARCHAR(255),
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
)

INSERT INTO users (username, password)
    VALUES
    ('simon', 'simonpass'),
    ('harry', 'harrypass');

SELECT username, id FROM users
    ORDER BY username ASC;