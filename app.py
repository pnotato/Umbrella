## I got help from the CS50.ai for the initialize page, on session.get, and initilizing the session dictionary
## https://www.w3schools.com/python/python_variables_global.asp
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

from helpers import weather, adjust, forecastpredict

app = Flask(__name__)
check = ""

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
    global check
    if request.method == "POST":
        check = weather(request.form.get("location"))

        if check != None:
            session['givenloc'] = check["name"]
            return redirect("/")

    if session.get('givenloc') == None:
        return render_template("initialize.html")
    else:
        location = weather(session['givenloc'])
        selection = adjust(location)
        if session.get('units') == "Imperial":
            currenttemp = location["far"]
            unit = "Fahrenheit"
        else:
            currenttemp = location["celsius"]
            unit = "Celsius"

        return render_template("index.html", location=location, selection=selection, currenttemp=currenttemp, unit=unit)

@app.route("/location", methods=["POST","GET"])
def location():
    if request.method == "POST":
        check = weather(request.form.get("location"))

        if check != None:
            session['givenloc'] = check["name"]
            return redirect("/")
        return redirect("/location")

    else:
        location = weather(session['givenloc'])
        if session.get('units') == "Imperial":
            currenttemp = location["far"]
            unit = "Fahrenheit"
        else:
            currenttemp = location["celsius"]
            unit = "Celsius"
        location = weather(session['givenloc'])
        return render_template("location.html", location=location, currenttemp=currenttemp, unit=unit)

@app.route("/forecast")
def forecast():
    location = weather(session['givenloc'])
    selection = adjust(location)
    forecast = forecastpredict(location)
    if session.get('units') == "Imperial":
        textunit = "F"
        locationunit = location["far"]
        forecastunit1 = forecast[0]['avgtempf']
        forecastunit2 = forecast[1]['avgtempf']
    else:
        textunit = "C"
        locationunit = location["celsius"]
        forecastunit1 = forecast[0]['avgtempc']
        forecastunit2 = forecast[1]['avgtempc']
    if session.get('units') == "Imperial":
        currenttemp = location["far"]
        unit = "Fahrenheit"
    else:
        currenttemp = location["celsius"]
        unit = "Celsius"

    return render_template("forecast.html", location=location, selection=selection,
                           forecast=forecast, unit=unit, textunit=textunit, locationunit=locationunit,
                             forecastunit1=forecastunit1, forecastunit2=forecastunit2, currenttemp=currenttemp)

@app.route("/units")
def units():
    ## default is Metric
    if request.method == "GET":
        if session.get('units') == "Imperial":
            session["units"] = "Metric"
        elif session.get('units') == "Metric":
            session["units"] = "Imperial"
        else:
            session["units"] = "Imperial"
        return redirect("/")

