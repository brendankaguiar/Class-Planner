#routes stored here
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Course, Transcript
from . import db
import json
f = open('Class-Planner/FlaskApp/website/courses.json')
data = json.load(f)
views = Blueprint('views', __name__)
@views.route('/', methods = ['GET', 'POST'])#home page decorator and route
@login_required#cannot get to homepage unless logged in
def home():#render home page
    if request.method == 'POST':
        Name = request.form.get('name')
        Credits = request.form.get('credits')
        Term = request.form.get('term')
        Expected_GPA = request.form.get('expected_gpa')
        Transcript_ID = Transcript.query.filter_by(user_id=current_user.id).first()
        flash("Course added",category ="success")
        new_Course = Course(
            name = Name, 
            credits = Credits, 
            term = Term, 
            expected_gpa = Expected_GPA,
            user_id=current_user.id,
            transcript_id = Transcript_ID
            )
        db.session.add(new_Course)
        db.session.commit()
    return render_template("home.html",user=current_user, jsonCourses=data)#user can be used in templates to reference user 
@views.route('/delete-Course',methods = ['POST'])
def delete_Course():
    Course = json.loads(request.data)
    CourseID = Course['CourseID']
    Course = Course.query.get(CourseID)
    if Course: 
        if Course.user_id == current_user.id:
            db.session.delete(Course)
            db.session.commit()
            return jsonify({})

