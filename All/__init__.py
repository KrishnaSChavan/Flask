from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'veryverysecreatkeycantbeshared'
# pip3 uninstall flask_sqlalchemy and pip3 install flask-sqlalchemy==2.5.1 if not able to create db
#app.config['SQLALCHEMY_MIGRATE_REPO'] = 'sqlite:///database/memb.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/all.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://abc:12345678@localhost:5432/logg'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
from All import routes
