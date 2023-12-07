DROP TABLE users CASCADE;
DROP TABLE citations CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password_hash TEXT
);
CREATE TABLE citations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    type TEXT,
    key TEXT,
    author TEXT,
    title TEXT,
    year INTEGER
);

INSERT INTO users (username, password_hash) VALUES ('admin', 'password');
\q