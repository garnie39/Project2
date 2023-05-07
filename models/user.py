import psycopg2
from models import common

class User:
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def get_user_if_valid(self):
        result = common.sql_read(f"SELECT * FROM users WHERE email=%s", [self.email])
        print(len(result))