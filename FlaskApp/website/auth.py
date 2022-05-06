#login route
#imports requests to and from the server
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Transcript
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user
auth = Blueprint('auth', __name__)
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()#filter user with matching email
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category ='success')
                login_user(user, remember = True)#login the user
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Try again', category='error')
        else:
            flash('Email does not exist.',category='error')
    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required#decorator that prevents access of this route unless the user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))#redirect to login page
    
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        newPassword = request.form.get('newPassword')
        passwordConfirm = request.form.get('passwordConfirm')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email exists.',category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
        elif len(first_name)  < 2:
            flash("Name must be longer than 2 characters", category='error')
        elif len(newPassword) < 7:
            flash("Password must be more thah 7 characters", category='error')
        elif newPassword != passwordConfirm:
            flash("Passwords don't match", category='error')
        else:
            #add user data to database
            new_user = User(
                email=email,
                first_name= first_name,
                password=generate_password_hash(newPassword,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            new_transcript = Transcript(user_id = current_user.id)
            db.session.add(new_transcript)
            db.session.commit()
            login_user(user, remember = True)#login the user
            flash("Account created", category='success')
            return redirect(url_for('views.home'))#redirect to home page
    return  render_template("signup.html", user = current_user)