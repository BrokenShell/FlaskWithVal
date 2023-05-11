from Fortuna import canonical
from flask import Flask, render_template, request
import pandas as pd

from app.database import Database

APP = Flask(__name__)
db = Database()


@APP.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("home.html", output=canonical())


@APP.route("/about")
def about_page():
    users = db.find({})
    df = pd.DataFrame(users)
    table = df.to_html(index=False)
    return render_template("about.html", table=table)


@APP.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = {
            "full_name": request.values.get("full_name"),
            "age": request.values.get("age", type=int),
            "profession": request.values.get("profession"),
        }
        db.insert(data)
    return render_template("contact.html")


@APP.route("/delete/<full_name>", methods=["GET", "DELETE"])
def delete(full_name: str):
    db.delete({"full_name": full_name})
    return "True"
