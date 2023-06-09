from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min = 6, max = 15)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Register', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min = 6, max = 15)])
    submit = SubmitField(label='Login', validators=[DataRequired()])

class ResetrequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField(label='Submit', validators=[DataRequired()])


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(),Length(min = 6, max = 15)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Change password', validators=[DataRequired()])