import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Set up the database connection
filepath = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(filepath, 'classes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Schedule1(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<classID %r>' % self.classID

class Schedule2(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<classID %r>' % self.classID        

class Schedule3(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<classID %r>' % self.classID

class Schedule4(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)

class Schedule5(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<classID %r>' % self.classID

class Schedule6(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<classID %r>' % self.classID        

class Schedule7(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<classID %r>' % self.classID

class Schedule8(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<classID %r>' % self.classID   

class Classes(db.Model):
    classID = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classAbv = db.Column(db.String(4))
    ClassNumber = db.Column(db.Integer)
    className = db.Column(db.String(200))
    classDescription = db.Column(db.String(200))
    ClassCredits = db.Column(db.Integer)
    ClassAvail = db.Column(db.Integer)

    def __repr__(self):
        return '<Name %r>' % self.ClassName


@app.route('/')
def index():
    title = "test"
    classSchedule = Classes.query.all()
    ScheduleF = Schedule1.query.all()
    ScheduleS = Schedule2.query.all()
    return render_template('drag.html', classSchedule=classSchedule, Schedule1=ScheduleF, Schedule2=ScheduleS,  title=title)
 
@app.route("/updateList",methods=["POST","GET"])
def updateList():
    return jsonify('Successfully Updated')
 
if __name__ == "__main__":
    app.run()