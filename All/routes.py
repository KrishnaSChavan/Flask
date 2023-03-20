from flask import Flask,render_template,redirect,url_for,flash,request
from All import app
from All.forms import LoginForm,RegisterForm
from pymysql import connections
from conf import *
import boto3

db_conn = connections.Connection(
   host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb
)
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
        emp_image_file = request. files ['emp_image_file']
        insert_sql = "INSERT INTO employe VALUES (%s, %s, %s, %s,%s)"
        cursor = db_conn.cursor()
        try:

            cursor.execute(insert_sql, (username, email, aadhar_no, password, id))
            db_conn.commit()
            
            emp_image_file_name_in_s3 = "emp-id-" + str(email) + "_image_file"
            s3 = boto3.resource('s3')

            try:
                print("Data inserted in MySQL RDS... uploading image to S3...")
                s3.Bucket(custombucket).put_object(Key=emp_image_file_name_in_s3, Body=emp_image_file)
                bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
                s3_location = (bucket_location['LocationConstraint'])

                if s3_location is None:
                   s3_location = ''
                else:
                  s3_location = '-' + s3_location

                object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                  s3_location,
                   custombucket,
                   emp_image_file_name_in_s3)

            except Exception as e:
               return str(e)

        finally:
            cursor.close()

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