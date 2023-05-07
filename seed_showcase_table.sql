DROP TABLE IF EXISTS showcase;

CREATE TABLE showcase(id SERIAL PRIMARY KEY, user_id BIGINT, pic_url TEXT, pic_name TEXT, is_bid BOOLEAN);