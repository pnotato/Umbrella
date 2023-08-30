from flask import Flask, redirect, render_template, request

from cs50 import sql

app = Flask(__name__)

@app.route("/")
def index():
    render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def edit():
    
    if request.method == "POST":
        return redirect("/edit")
    
    else:
        return render_template("edit.html", 400)