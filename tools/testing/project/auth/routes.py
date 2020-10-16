from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user

from project import app, db, bcrypt
from project.models import User
from project.auth.forms import RegistrationForm, LoginForm

auth = Blueprint("auth", __name__)

@auth.route("/auth/register", methods=["GET", "POST"])
def register():
  if current_user.is_authenticated:
    flash("You're already authenticated.", "warning")
    return redirect(url_for("main.home"))
  
  form = RegistrationForm()
  
  if form.validate() and form.register.data:
    hashed_password = bcrypt.generate_password_hash(form.password.data)
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    flash("Account successfully created.", "success")
    return redirect(url_for("auth.login"))
  
  return render_template("auth/register.html", form=form, title="Register")

@auth.route("/auth/login", methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
    flash("You're already authenticated.", "warning")
    return redirect(url_for("main.home"))
  
  form = LoginForm()
  
  if form.validate() and form.login.data:
    user = User.query.filter_by(username=form.username.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user)
      flash("Login successful.", "success")
      next_page = request.args.get("next")
      return redirect(next_page) if next_page else redirect(url_for("main.home"))
    else:
      flash("You've entered the wrong credentials.", "error")
      return redirect(url_for("auth.login"))
  
  return render_template("auth/login.html", form=form, title="Login")

@auth.route("/auth/logout")
def logout():
  logout_user()
  return redirect(url_for("auth.login"))