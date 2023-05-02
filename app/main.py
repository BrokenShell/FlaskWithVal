from Fortuna import canonical
from flask import Flask, render_template


APP = Flask(__name__)


@APP.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("home.html", output=canonical())
