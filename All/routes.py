from flask import Flask,render_template,redirect,url_for,flash,request
from All import app,bcrypt,db,mail
from All import *
from All.forms import LoginForm,RegisterForm,ResetrequestForm,ResetPasswordForm
from All.models import User
from flask_login import login_user,logout_user,current_user,login_required
from flask_mail import Message

file_name = ''


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

def send_mail(user):
    token = user.get_token()
    msg = Message('Password Reset',recipients=[user.email],sender='kc756953@gmail.com')
    msg.body=f'''Reset Password follow link below
    
    {url_for('reset_token', token=token,_external=True)}
    
    '''
    mail.send(msg)

@app.route("/reset_request",methods = ['POST','GET'])
def reset_request():
    form = ResetrequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_mail(user)
            flash('Request sent. Check your mail','success')
            return redirect(url_for("login"))
    return render_template("reset_request.html",title="Reset",form=form)


@app.route('/reset_password/<token>',methods=['POST','GET'])
def reset_token(token):
    user = User.verify_token(token)
    if user is None:
        flash('Invalid token','warning')
        return redirect(url_for('reset_request'))
    
    form = ResetPasswordForm()

    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8') 
        user.password = hashed_password
        db.session.commit()
        flash('Password changed','success')
        return redirect(url_for('login'))
    return render_template('change_pass.html',title='Reset Password',legend='change_password',form=form)