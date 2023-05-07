from flask import Flask, render_template, request, redirect, session
# import os
from models import user, showcase
# from dotenv import load_dotenv
# load_dotenv()


app = Flask(__name__)

# @app.route('/')
# def index():
#     # connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
#     connection = psycopg2.connect(dbname='project2', user='postgres', port=5433, password='Puppygarn3939!')
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM users;")
#     results = cursor.fetchall()
#     connection.close()
#     return f"{results[0]}"


@app.route("/signup")
def signup():
    return render_template("signup.html")
# CREATE
@app.route("/signup", methods=["POST"])
def signup_action():
    user.add_user(request.form.get('username'),request.form.get('email'),request.form.get('password'))
    return redirect("/login")

@app.route("/login")
def login_form():
    return render_template("login.html")
# READ
@app.route("/login", methods=["POST"])
def login_action():
    email = request.form.get('email')
    password = request.form.get('password')

    curr_user = user.get_user_if_valid(email, password)

    if curr_user:
        session["user_id"] = curr_user["id"]
        session["user_username"] = curr_user["username"]
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
    app.run(debug=True) #,port=os.getenv("PORT", default=5000)
