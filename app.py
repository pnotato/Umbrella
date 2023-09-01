## I got help from the CS50.ai for the initialize page, on session.get, and initilizing the session dictionary

from flask import Flask, redirect, render_template, request, session
from flask_session import Session

from helpers import weather

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        location = weather(request.form.get("location"))             ## calls the api function

        if location != None:                                        ## as long as theres a match
            session['givenloc'] = True                              ## give access to the index page and refresh
            return redirect("/")

    if session.get('givenloc') == None:                             ## if there was no match, go back to the initialize page
        return render_template("initialize.html")
    else:                                                           ## elsewise, go to the index.
        return render_template("index.html")

@app.route("/location", methods=["POST","GET"])
def location():
    if request.method == "POST":
        return redirect("/location")
    else:
        return render_template("location.html")

