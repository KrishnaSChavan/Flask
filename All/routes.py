from flask import Flask,render_template
from All import app

@app.route("/")
@app.route("/home")
def home():
    return render_template("Homepage.html",title="Home",NAME='Home')


@app.route("/about")
def about():
    return render_template("Homepage.html",title="About",NAME="About")

@app.route("/account")
def account():
    return render_template("Account_page.html",title="Account",NAME="Account")