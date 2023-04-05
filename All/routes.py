from flask import Flask,render_template,redirect,url_for,flash,request
from All import app,bcrypt,db
from All import *
from All.forms import LoginForm,RegisterForm,ResetrequestForm
from All.models import User
from flask_login import login_user,logout_user,current_user,login_required
@app.route("/")
@app.route("/home")
def home():
    return render_template("Homepage.html",title="Home")


@app.route("/about")
def about():
    return render_template("About.html",title="About")

@app.route("/department")
def department():
    return render_template("Homepage.html",title="Department")


@app.route("/account")
@login_required
def account():
    return render_template("Account_page.html",title="Account")


@app.route("/register",methods = ['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegisterForm()
    if form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User (username=form.username.data,email=form.email.data , password=encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash(f'You have successfully registered {form.username.data}',category='success')
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods = ['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            user = User.query.filter_by(email=form.email.data).first()
            if form.email.data == user.email and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user)
                flash(f'You have successfully loggedin as {user.username}',category='success')
                return redirect(url_for("account"))
            else:
                flash('Invalid password',category='danger')
        else:
            flash('Invalid email',category='danger')
            
    return render_template("login.html",title="Login",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html",title="Dashboard")


@app.route("/reset_request",methods = ['POST','GET'])
def reset_request():
    form = ResetrequestForm()
    return render_template("reset_request.html",title="Reset",form=form)