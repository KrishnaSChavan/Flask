from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
from All import routes
