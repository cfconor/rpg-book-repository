import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
if os.path.exists("env/env.py"):
    import env.env





app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo_obj = PyMongo(app)




@app.route("/")
@app.route("/catalog")
def catalog():
    articles = list(mongo_obj.db.articles.find())
    return render_template("catalog.html", articles=articles)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo_obj.db.users.find_one(
                {"username": request.form.get("username").lower()})

        if existing_user:
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_privileges": "user"
        }

        mongo_obj.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()

        return redirect(url_for("catalog"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo_obj.db.users.find_one(
                        {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed pw matches entered
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("catalog"))

            else:
                # invalid pw check
                return redirect(url_for("login"))

        else:
            # username doesnt exist
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_article", methods=["GET", "POST"])
def add_article():
    
    if request.method == "POST":
        today = date.today()
        created_date = today.strftime("%d/%m/%Y")
        article = {
            "article_name": request.form.get("article_name"),
            "article_author": request.form.get("article_author"),
            "article_link": request.form.get("article_link"),
            "article_category": request.form.get("article_category"),
            "game_system": request.form.get("game_system"),
            "created_date": created_date,
            "created_by": session["user"],
            "tags": [""] # this may need to be removed if there is no clean way to implement it
        }
        mongo_obj.db.articles.insert_one(article)
        return redirect(url_for("catalog"))


    article_categories = mongo_obj.db.categories.find().sort("category_name", 1)
    game_systems = mongo_obj.db.game_systems.find().sort("game_systems", 1)
    return render_template("add_article.html", categories=article_categories, game_systems=game_systems)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)