from flask import Flask,render_template,redirect,url_for,flash,request
from All import app
from All import *
from All.forms import LoginForm,RegisterForm
from All.models import User,Memb
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
        user = User (username=form.username.data,email=form.email.data , password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'You have successfully registered {form.username.data}',category='success')
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            user = User.query.filter_by(email=form.email.data).first()
            if form.email.data == user.email and form.password.data == user.password:
                flash(f'You have successfully loggedin {form.email.data}',category='success')
                return redirect(url_for("account"))
            else:
                flash('Invalid password',category='danger')
        else:
            flash('Invalid email',category='danger')
            
    return render_template("login.html",title="Login",form=form)

@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html",title="Dashboard")