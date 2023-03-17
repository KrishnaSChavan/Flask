from flask import Flask,render_template,redirect,url_for,flash
from All import app
from All.forms import LoginForm,RegisterForm
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
@app.route("/account")
def account():
    return render_template("Account_page.html",title="Account")
@app.route("/register",methods = ['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('You have successfully registered',category=success)
        return redirect(url_for("home"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == '123@qwe.asd' and form.password.data == '123456789':
            flash('You have successfully registered',category=success)
            return redirect(url_for("account"))
        else:
            return redirect(url_for("home"))
    return render_template("login.html",title="Login",form=form)

@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html",title="Dashboard")