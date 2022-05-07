from cgi import test
import os
import sqlite3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Set up the database connection
filepath = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(filepath, 'classes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Set up dictionary to hold semester classes

semModified = [0b00000000]
scheduleClasses = {
"sem1Set": set(),
"sem2Set": set(),
"sem3Set": set(),
"sem4Set": set(),
'sem5Set': set(),
"sem6Set": set(),
"sem7Set": set(),
"sem8Set": set()
}


#update the scheduleClasses dict with modified classes set that semester as modified to mark that semester needs to be updated in the database
def updateClasses(postStr, scheduleDict, semModified):
    x = postStr.index("From")
    changedSem = postStr[x+5]
    changedSet = set()
    x = postStr.find("]'")
    while x != -1:
        postStr = postStr[x+5:]
        x = postStr.index("'")
        changedSet.add(int(postStr[:x]))
        x = postStr.find("]'")
    scheduleDict.update({f"sem{changedSem}Set": changedSet})
    strMod = "0b1"
    for num in range(int(changedSem) -1):
        strMod += "0"
    semModified[0] = semModified[0] | int(strMod,2)



dbLock = False
def pushToDatabase(scheduleClasses, semModified):
    global dbLock
    ph = 0
    while dbLock == True:
       ph = 0 
    dbLock = True    
    connection = sqlite3.connect('classes.db')
    cursor = connection.cursor()
    modified = str(bin(semModified[0]))
    count = 1
    for changed in modified[2:][::-1]:
        if changed == '1':
            cursor.execute(f"DELETE FROM Schedule{count}")
            if len(scheduleClasses[f"sem{count}Set"]) != 0:
                for classID in scheduleClasses[f"sem{count}Set"]:
                    cursor.execute(f"INSERT INTO Schedule{count} (classID) VALUES ({classID});")
                    #print(f"INSERT INTO Schedule{count} (classID) VALUES ({classID});")
                scheduleClasses.update({f"sem{count}Set": set()})
        count += 1
    semModified[0] = 0b0
    connection.commit()
    dbLock = False


    


class Schedule1(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)
    className = db.Column(db.String(200))

    def __repr__(self):
        return '<classID %r>' % self.classID

class Schedule2(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)
    className = db.Column(db.String(200))

    def __repr__(self):
        return '<classID %r>' % self.classID        

class Schedule3(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)
    className = db.Column(db.String(200))

    def __repr__(self):
        return '<classID %r>' % self.classID

class Schedule4(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)
    className = db.Column(db.String(200))

class Schedule5(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)
    className = db.Column(db.String(200))

    def __repr__(self):
        return '<classID %r>' % self.classID

class Schedule6(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)
    className = db.Column(db.String(200))

    def __repr__(self):
        return '<classID %r>' % self.classID        

class Schedule7(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)
    className = db.Column(db.String(200))

    def __repr__(self):
        return '<classID %r>' % self.classID

class Schedule8(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement='auto', nullable=False, unique=True)
    classID = db.Column(db.Integer, nullable=False)
    className = db.Column(db.String(200))

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
    schedule1 = Schedule1.query.all()
    schedule2 = Schedule2.query.all()
    schedule3 = Schedule3.query.all()
    schedule4 = Schedule4.query.all()
    schedule5 = Schedule5.query.all()
    schedule6 = Schedule6.query.all()
    schedule7 = Schedule7.query.all()
    schedule8 = Schedule8.query.all()
    return render_template('drag.html', classSchedule=classSchedule, Schedule1=schedule1, Schedule2=schedule2, Schedule3=schedule3, Schedule4=schedule4,Schedule5=schedule5, Schedule6=schedule6, Schedule7=schedule7, Schedule8=schedule8, title=title)
 
@app.route("/updateList",methods=["POST","GET"])
def updateList():
    if request.method == 'GET':
        return "posting url"
    if request.method == 'POST':
        sentData = None
        sentData = request.form
        dataStr = str(sentData)
        print(dataStr)
        updateClasses(dataStr, scheduleClasses, semModified)
        pushToDatabase(scheduleClasses, semModified)
        return "post"
 
if __name__ == "__main__":
    app.run()