from flask import Flask, render_template, request, redirect, session, jsonify
import os
import psycopg2
from models import user, showcase

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
    email = request.form.get('email')
    password = request.form.get('password')

    n_user = user.User(email=email, password=password)
    n_user = n_user.get_user_if_valid()

    if n_user:
        session["user_id"] = n_user["id"]
        session["user_email"] = n_user["email"]
        return redirect("/feed")
    else:
        return render_template("login.html", message = "Invalid account! Try again or If you haven't register, please sign up!")
    
@app.route("/logout")
def logout():
    session["user_id"] = None
    session["user_username"] = None
    return redirect("/feed")

# READ
@app.route("/")
def feed():
    showcase_obj = showcase.Posts()
    dict = showcase_obj.get_all_posts()
    return render_template("feed.html", feed_item = dict)

# CREATE
@app.route("/form/newpost")
def new_post():
    return render_template("newpost.html")

@app.route("/api/newpost", methods=["POST"])
def add_new_post():
    form = request.form

    new_post = showcase.Posts(
        user_id = session("user_id"),
        pic_url = form.get("pic_url"),
        pic_name = form.get("pic_name"),
        is_bid = form.get("bid")
    )

    new_post.new_post()

    return redirect("/feed")

# UPDATE
@app.route("/form/post/edit/<id>")
def edit_post_form(id):
    if session.get("user_id", ""):
        showcase_obj = showcase.Posts(id=id)
        return render_template("edit_post.html", post = showcase.get_post())
    else:
        return redirect("/feed")

@app.route("/post/edit/<id>", methods=["POST"])
def edit_post(id):
    form = request.form
    post_obj = showcase.Posts(id=id)
    post_obj.edit_post(form.get("pic_name"), form.get("is_bid"))
    return redirect("/feed")

# DELETE
@app.route("/form/post/delete/<id>")
def delete_form(id):
    post_selected = showcase.Posts(user_id=request.form.get("user_id"))
    if (session.get("user_id") == post_selected) and (is_bid == "False"):
        if session.get("user_id", ""):
            post_obj = showcase.Posts(id=id)
            return render_template("delete_post.html", post = post_obj.get_post())
    else:
        return redirect ("/feed")

@app.route("/post/delete", methods=["POST"])
def delete_post():
    post_obj = showcase.Posts(id=request.form.get("id"))
    post_obj.delete_post()
    return redirect ("/feed")

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("PORT", default=5000))
