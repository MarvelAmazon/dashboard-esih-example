from flask import render_template
from . import auth

@auth.route("/")
def index():
    return render_template("dashboard/index.html")

@auth.route("/index")
def index2():
    return "Hello World ... 1!"