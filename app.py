import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


@app.route("/add_article", methods=["GET", "POST"])
def add_article():
    # setting some default values until further functionality added
    session["username"] = "conor"

    if request.method == "POST":
        today = date.today()
        created_date = today.strftime("%d/%m/%Y")
        article = {
            "article_name": request.form.get("article_name"),
            "article_author": request.form.get("article_author"),
            "article_category": request.form.get("article_category"),
            "game_system": request.form.get("game_system"),
            "created_date": created_date,
            "created_by": session["username"],
            "tags": [""] # this may need to be removed if there is no clean way to implement it
        }
        mongo.db.tasks.insert_one(article)
        return redirect(url_for("catalog"))


    article_categories = mongo_obj.db.categories.find().sort("category_name", 1)
    game_systems = mongo_obj.db.game_systems.find().sort("game_systems", 1)
    return render_template("add_article.html", categories=article_categories, game_systems=game_systems)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)