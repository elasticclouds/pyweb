from flask import Flask, render_template, request, jsonify
from datetime import date


pyweb = Flask(__name__)


@pyweb.route("/")
def home():
    return render_template("home.html")

@pyweb.route("/aboutme")
def about():
    return render_template("index.html")

@pyweb.route("/time")
def time():
    day = date.today().day.__str__()
    month = date.today().month.__str__()
    year = date.today().year.__str__()
    return month + "/" +  day + "/" + year

pyweb.run()
