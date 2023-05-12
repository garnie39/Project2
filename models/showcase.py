from models import common

class Posts:
    def __init__(self, id=0, user_id=None, pic_url=None, pic_name=None, is_bid=None, user_like=None, comment=None, username=None):
        self.id = id
        self.user_id = user_id
        self.pic_url = pic_url
        self.pic_name = pic_name
        self.is_bid = is_bid
        self.user_like = user_like
        self.comment = comment
        self.username = username

    def convert_to_dict(self, post):
        return {
            "id": str(post[0]),
            "user_id": str(post[1]),
            "username": post[2],
            "pic_url": post[3],
            "pic_name": post[4],
            "is_bid": post[5],
            "user_like": str(post[6]),
            "comment": post[7]
        }

    def get_all_posts(self):
        all_posts = common.sql_read("SELECT * FROM showcase;")
        return [self.convert_to_dict(post) for post in all_posts]
    
    def get_post(self):
        post = common.sql_read("SELECT * FROM showcase WHERE id=%s;", [self.id])[0]
        return self.convert_to_dict(post)

    def likes(self):
        pass
    
    def get_edit_post(self):
        post = common.sql_read2("SELECT * FROM showcase WHERE id=%s AND is_bid=%s;", [self.id, False])
        return self.convert_to_dict(post)

    def edit_post(self, new_pic_name, new_is_bid):
        common.sql_write(f"UPDATE showcase SET pic_name=%s, is_bid=%s WHERE id={self.id};", [new_pic_name, new_is_bid])

    def new_post(self):
        common.sql_write("INSERT INTO showcase (user_id, pic_url, pic_name, is_bid, username) VALUES(%s,%s,%s,%s,%s);", [self.user_id, self.pic_url, self.pic_name, self.is_bid, self.username])

    def delete_post(self):
        common.sql_write("DELETE FROM showcase WHERE id=%s AND is_bid=%s;", [self.id, False])


class Bids:
    def __init__(self, id=0, user_id=None, pic_url=None, pic_name=None, is_bid=None, user_like=None, comment=None, username=None):
        self.id = id
        self.user_id = user_id
        self.pic_url = pic_url
        self.pic_name = pic_name
        self.is_bid = is_bid
        self.user_like = user_like
        self.comment = comment
        self.username = username

    def convert_to_dict(self, post):
        return {
            "id": str(post[0]),
            "user_id": str(post[1]),
            "pic_url": post[3],
            "pic_name": post[4],
            "is_bid": post[5],
            "user_like": str(post[6]),
            "comment": post[7],
            "username": post[2]
        }

    def get_all_bids(self):
        all_posts = common.sql_read("SELECT * FROM showcase WHERE is_bid=%s;", [True])
        return [self.convert_to_dict(post) for post in all_posts] 

    def user_bid(self):
        pass
