from flask import Flask,render_template
from All import app

@app.route("/")
def index():
    return "Hello World!"
@app.route("/home")
def home():
    return render_template("Homepage.html",title="Home")


@app.route("/about")
def about():
    return render_template("Homepage.html",title="About")

@app.route("/account")
def account():
    return render_template("Account_page.html",title="Account")