import bcrypt
from models import common

class User:
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def get_user_if_valid(self):
        results = common.sql_read(f"SELECT * FROM users WHERE email=%s", [self.email])
        if len(results):
            user = results[0]
            user_formatted = {"id": user[0], "username": user[1], "email": user[2], "hashed_password": user[4]}
            if bcrypt.checkpw(self.password.encode(), user_formatted["hashed_password"].encode()):
                return user_formatted
            return None
        return None
    
    def add_user(self):
        hashed_password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt().decode())
        common.sql_write("INSERT INTO users (username, email, hashed_password, coins) VALUES(%s,%s,%s, %s)", [self.username, self.email, hashed_password, 20])