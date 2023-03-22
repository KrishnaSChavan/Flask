from All import db
from All import * 
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer , primary_key=True) 
    username=db.Column(db.String(20) , unique=True, nullable=False) 
    email=db.Column (db.String(120) , unique=True, nullable=False) 
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg') 
    password=db.Column(db.String(20) ,nullable=False) 
    date_created=db.Column (db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.username} : {self.email} : {self.date_created}'
    

class Memb(db.Model):
    username=db.Column(db.Integer ) 
    email=db.Column(db.String(40) , unique=True, nullable=False) 
    aadhar_no=db.Column (db.String(14) , primary_key=True, unique=True, nullable=False) 
    password=db.Column(db.String(200) ,nullable=False)
    id=db.Column(db.Integer, nullable=False)
    date_created=db.Column (db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.username} : {self.email} : {self.date_created}'