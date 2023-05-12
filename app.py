from flask import Flask, render_template, request, redirect, session
import os
import psycopg2
from models import user, showcase, common

app = Flask(__name__)
app.config["SECRET_KEY"] = "My secret key"

@app.route("/signup")
def signup():
    return render_template("signup.html")

# CREATE
@app.route("/signup", methods=["POST"])
def signup_action():
    new_user = user.User(request.form.get('username'),request.form.get('email'),request.form.get('password'))
    new_user.add_user()

    return redirect("/login")

@app.route("/login")
def login_form():
    return render_template("login.html")

# READ
@app.route("/login", methods=["POST"])
def login_action():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    n_user = user.User(username=username, email=email, password=password)
    n_user = n_user.get_user_if_valid()

    if n_user:
        session["user_id"] = n_user["id"]
        session["user_username"] = n_user["username"]
        session["user_email"] = n_user["email"]
        return redirect("/")
    else:
        return render_template("login.html", message = "Invalid account! Try again or If you haven't register, please sign up!")
    
@app.route("/logout")
def logout():
    session["user_id"] = None
    session["user_username"] = None
    return redirect("/")

# READ
@app.route("/")
def feed():
    showcase_obj = showcase.Posts()
    dict = showcase_obj.get_all_posts()
    for dic in dict:
        bid = dic['is_bid']
        # print(bid)
    return render_template("feed.html", feed_item = dict, result = bid)

# CREATE
@app.route("/form/newpost")
def new_post():
    return render_template("newpost.html")

@app.route("/newpost", methods=["POST"])
def add_new_post():
    new_post = showcase.Posts(
        user_id = session["user_id"],
        username = session["user_username"],
        pic_url = request.form.get("pic_url"),
        pic_name = request.form.get("pic_name"),
        is_bid = request.form.get("bid")
    )
    new_post.new_post()
    
    return redirect("/")

# UPDATE
@app.route("/likes/add/<id>")
def add_like(id):
    post = showcase.Posts(id=id)
    item = post.get_post()
    current = item['user_like']
    current_like = current.split(',')
    current_like.append(str(session['user_id']))
    current_like_str = ','.join(current_like)
    print(current_like)
    like = common.sql_write("UPDATE showcase SET user_like=%s WHERE id=%s;", [current_like, id])
    result = post.get_post()
    print(result)
    return render_template("feed.html")

# READ
@app.route("/<username>/")
def user_page_post(username):
    user_id = session['user_id']
    user_posts = common.sql_read("SELECT * FROM showcase WHERE user_id=%s AND is_bid=%s;", [user_id, False])
    all_posts = showcase.Posts()
    all_user_posts = [all_posts.convert_to_dict(post) for post in user_posts] 
    return render_template("profile_post.html", user_posts = all_user_posts)
        
# READ
@app.route("/<username>/bid")
def user_page_bid(username):
    user_id = session['user_id']
    user_posts = common.sql_read("SELECT * FROM showcase WHERE user_id=%s AND is_bid=%s;", [user_id, True])
    all_posts = showcase.Posts()
    all_user_posts = [all_posts.convert_to_dict(post) for post in user_posts] 
    return render_template("profile_bid.html", user_posts = all_user_posts)
        
# UPDATE
@app.route("/form/edit/<id>")
def edit_post_form(id):
    post_selected = showcase.Posts(id=request.form.get("id"))
    if session.get("user_id", ""):
        post_obj = showcase.Posts(id=id)
        post = post_obj.get_edit_post()
        print(post)
        return render_template("edit_post.html", post = post)
    else:
        return render_template("error.html", message="You are not authorized to edit this post.")
    
@app.route("/post/edit/<id>", methods=["POST"])
def edit_post():
    form = request.form
    post_obj = showcase.Posts(id=form.get("id"))
    post_obj.edit_post(form.get("pic_name"), forrm.get("bid"))
    return redirect("/")

# DELETE
@app.route("/form/delete/<id>")
def delete_form(id):
    if session.get("user_id", ""):
        post_obj = showcase.Posts(id=id)
        post = post_obj.get_post()
        if post['user_id'] == session["user_id"] and post['is_bid'] == "False":
            return render_template("delete.html", post=post)
        else:
            return render_template("error.html", message="You are not authorized to delete this post.")
    else:
        return redirect ("/")

@app.route("/post/delete", methods=["POST"])
def delete_post():
    form = request.form
    post_obj = showcase.Posts(id=form.get("id"), user_id=form.get("user_id"))
    if form.get("user_id") == session.get("user_id", "") and post['is_bid'] == "False":
        post_obj.delete_post()
        return redirect ("/")
    else:
        return render_template("error.html", message="You are not authorized to delete this post.")

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("PORT", default=5000))
