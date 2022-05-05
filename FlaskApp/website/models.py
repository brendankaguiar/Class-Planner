from . import db#import database into model
from flask_login import UserMixin#object to help users log in
from sqlalchemy.sql import func #used to automate datefield

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))#could be text
    credits = db.Column(db.Integer)
    term = db.Column(db.String(20))
    expected_gpa = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    transcript_id = db.Column(db.Integer, db.ForeignKey('transcript.id'))

class User(db.Model,UserMixin):#setup user model for login
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)#invalid to make existing email
    password =db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    courses = db.relationship('Course')
    transcript = db.relationship('Transcript')


class Transcript(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courses = db.relationship('Course')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    