from models import common

class Showcase:
    def __init__(self, id=0, user_id=None, pic_url=None, pic_name=None, is_bid=None):
        self.id = id
        self.user_id = user_id
        self.pic_url = pic_url
        self.pic_name = pic_name
        self.is_bid = is_bid

    def convert_to_dict(self, post):
        return {
            "id": str(post[0]),
            "user_id": str(post[1]),
            "pic_url": post[2],
            "pic_name": post[3],
            "is_bid": post[4]
        }

    def get_all_showcase(self):
        all_posts = common.sql_read("SELECT * FROM showcase;")
        return [self.convert_to_dict(post) for post in all_posts]
    
    def get_post(self):
        post = common.sql_read("SELECT * FROM showcase WHERE id=%s;", [self.id])[0]
        return self.convert_to_dict(post)

    def new_post(self):
        common.sql_write("INSERT INTO showcase (user_id, pic_url, pic_name, is_bid) VALUES(%s,%s,%s,%s);", [self.user_id], self.pic_url, self.pic_name, self.is_bid)

    def edit_post(self, n_name, n_is_bid):
        common.sql_write(f"UPDATE showcase SET name=%s, is_bid=%s WHERE id={self.id};", [n_name, n_is_bid])

    def delete_post(self):
        common.sql_write(f"DELETE FROM showcase WHERE id={self.id};")