DROP TABLE IF EXISTS users;

CREATE TABLE users(id SERIAL PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, hashed_password TEXT NOT NULL, coins INT, profile_pic TEXT);