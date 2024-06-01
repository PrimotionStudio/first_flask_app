from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip().lower()
        password = request.form.get('password')
        if username == "" or password == "":
            flash("Please fill all fields")
        else:
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in successfully")
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash("Incorrect password")
            else:
                flash("User does not exist")

    return render_template("login.html")


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = dict(request.form)
        username = data.get("username").strip().lower()
        email = data.get("email").strip().lower()
        password = data.get("password")
        user = User.query.filter(
            (User.username == username) | (User.email == email)).first()
        if user:
            flash("Username or email already taken")
        elif username == "" or email == "" or password == "":
            flash("Please fill all fields")
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(
                password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created")
            return redirect(url_for('auth.login'))
    return render_template("signup.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
