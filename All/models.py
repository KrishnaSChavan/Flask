from All import db,login_manager,app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from All import *
from datetime import datetime
from flask_login import UserMixin
from flask import redirect,url_for

@login_manager.user_loader

def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler 
def unauthorized() :
    
    return redirect(url_for('register'))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer , primary_key=True) 
    username=db.Column(db.String(20) , unique=True, nullable=False) 
    email=db.Column (db.String(120) , unique=True, nullable=False) 
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg') 
    password=db.Column(db.String(60) ,nullable=False) 
    date_created=db.Column (db.DateTime, default=datetime.utcnow)

    def get_token(self,expires_sec=300):
        serial  = Serializer(app.config['SECRET_KEY'],expires_in=expires_sec)
        return serial.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_token(self,token):
        serial  = Serializer(app.config['SECRET_KEY'])
        try:
            serial.load(token)['user_id']
        except:
            return None
        return User.query.get(self.user_id)

    def __repr__(self):
        return f'{self.username} : {self.email} : {self.date_created.strftime("%d/%m/%Y, %H:%M:%S" )}'

class members(db.Model,UserMixin):
    __tablename__ = 'members'
    aadhar = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email=db.Column (db.String(120) , unique=True, nullable=False)
    password=db.Column(db.String(60) ,nullable=False) 
    date_created=db.Column (db.DateTime, default=datetime.utcnow)


    def __repr__(self) :
        return f'{self.username} : {self.email} : {self.date_created.strftime("%d/%m/%Y, %H:%M:%S" )}'