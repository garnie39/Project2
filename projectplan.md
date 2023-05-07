NFT + IG = +A SHOWCASE

1. sign up - log in

   - set sign up & log in page .html
   - function for sign up .py
   - function for logg in .py
     - rmb to hashed password
   - create table users
     - id SERRIAL PRIMARY KEY
     - username TEXT
     - user email TEXT NOT NULL
     - user password TEXT NOT NULL
     - user_credit_coins INT
     - user_profile_pic TEXT
     - hashed_password

2. main html page

   - <nav> .html
     - user page
       - user_credit
       - user_post
         - showcase
         - bid
       - user_profile_pic
     - feed
       - all users posts
     - bid
       - all bid posts
     - add credit coins
       - info how to add coin
     - about SHOWCASE
     - user_bid
       - list of successful bid
       - list of ongoingg bid
   - display .html
     - user_credit_coin
     - add post
     - feed
   - function to display all posts .py
   - function to display user_credit_coin .py
   - function to add post .py
   - CREATE TABLE showcase
     - id SERRIAL PRIMARY KEY
     - username TEXT
     - img TEXT
     - is_bid BOOLEAN
       - start time
       - end time

3. A post .html
   - like button .html
   - bid button .html
   - comment input
   - function to store all like n comment input .py
   - function to display likes and comments .py & .html
   - CREATE TABLE posts
     - id SERRIAL PRIMARY KEY
     - user_id TEXT
     - comment TEXT
     - is_like BOOLEAN
     - is_bid BOOLEAN
