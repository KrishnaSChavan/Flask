from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegisterForm(FlaskForm):
    username = StringField(lable ='Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    aadhar_no = StringField('Aadhar Number', validators=[DataRequired(),Length(min = 12, max = 12)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min = 6, max = 15)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')