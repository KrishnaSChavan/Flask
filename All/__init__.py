from flask import Flask
from pymysql import connections

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


from All import routes
