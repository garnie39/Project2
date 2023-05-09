from flask import Flask, render_template, request, redirect, session
import os
import psycopg2
from models import user, showcase

app = Flask(__name__)

@app.route('/')
def index():
    connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    results = cursor.fetchall()
    connection.close()
    return f"{results[0]}"


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

    curr_user = user.User(email=email, password=password)
    curr_user = curr_user.get_user_if_valid()

    if curr_user:
        session["user_id"] = curr_user["id"]
        session["user_name"] = curr_user["username"]
        return redirect("/feed")
    else:
        return render_template("login.html", message = "Invalid account! Try again or If you haven't register, please sign up!")
    
@app.route("/logout")
def logout():
    session["user_id"] = None
    session["user_username"] = None
    return redirect("/feed")

# READ
@app.route("/feed")
def feed():
    showcase_obj = showcase.Showcase()
    dict = showcase_obj.get_all_showcase()
    return render_template("feed.html", feed_item = dict)

# CREATE
@app.route("/form/newpost")
def new_post():
    return render_template("newpost.html")

@app.route("/api/newpost", methods=["POST"])
def add_new_post():
    form = request.form

    new_post = showcase.Showcase(
    user_id = session["user_id"],
    pic_url = form.get("pic_url"),
    pic_name = form.get("pic_name"),
    is_bid = form.get("bid")
    )

    new_post.new_post()

    return redirect("/feed")



if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("PORT", default=5000))
