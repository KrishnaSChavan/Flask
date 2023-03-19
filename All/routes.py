from flask import Flask,render_template,redirect,url_for,flash,request
from All import app
from All.forms import LoginForm,RegisterForm
from pymysql import connections
#from conf import *

#db_conn = connections.Connection(
#   host=customhost,
#    port=3306,
#    user=customuser,
#    password=custompass,
#    db=customdb

#)
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
        flash(f'You have successfully registered {form.username.data}',category='success')
        username = request.form['username']
        email = request.form['email']
        aadhar_no = request.form['aadhar_no']
        password = request.form['password']
        id = 2
        insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s,%s)"
        #cursor = db_conn.cursor()
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == '123@qwe.asd' and form.password.data == 'pppppppp':
            flash(f'You have successfully loggedin {form.email.data}',category='success')
            return redirect(url_for("account"))
        else:
            flash('Invalid email or password',category='danger')   
            
    return render_template("login.html",title="Login",form=form)

@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html",title="Dashboard")