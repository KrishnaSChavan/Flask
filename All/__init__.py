from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/member.db'
db = SQLAlchemy(app)

from All import routes
