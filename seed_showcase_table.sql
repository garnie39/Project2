DROP TABLE IF EXISTS showcase;

CREATE TABLE showcase(id SERIAL PRIMARY KEY, user_id BIGINT, username TEXT, pic_url TEXT, pic_name TEXT, is_bid BOOLEAN, user_like TEXT, comment TEXT);