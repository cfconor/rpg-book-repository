import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env/env.py"):
    import env.env

print(os.environ.get("IP"))

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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)