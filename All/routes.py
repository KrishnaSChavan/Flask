from flask import Flask,render_template
from All import app

@app.route("/")
@app.route("/home")
def home():
    return render_template("Homepage.html",title="Home")


@app.route("/about")
def about():
    return render_template("About.html",title="About")

@app.route("/department")
def department():
    return render_template("Department.html",title="Department")

@app.route("/register")
def register():
    return render_template("register.html",title="Register ")

@app.route("/login")
def login():
    return render_template("login.html",title="Login")

@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html",title="Dashboard")