import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
if os.path.exists("env/env.py"):
    import env.env

print(os.environ.get("IP"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)