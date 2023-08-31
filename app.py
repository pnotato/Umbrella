from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/edit", methods=["POST","GET"])
def edit():
    if request.method == "POST":
        return redirect("/edit")
    else:
        return render_template("edit.html")
    
f