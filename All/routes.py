from flask import Flask,render_template
from All import app

@app.route("/")
def index():
    return "Hello World!"
@app.route("/home")
def home():
    return render_template("home.html")