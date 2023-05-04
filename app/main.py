import requests
from Fortuna import canonical
from flask import Flask, render_template


APP = Flask(__name__)


@APP.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("home.html", output=canonical())


@APP.route("/about")
def about_page():
    return render_template("about.html", test="Hello, world")


@APP.route("/contact")
def contact_page():
    response = requests.post("https://themis-vector-db.herokuapp.com/version")
    return render_template("contact.html", version=response.json())
