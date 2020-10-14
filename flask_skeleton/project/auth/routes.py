from flask import Blueprint, render_template

from project import app
from project.models import User
from project.auth.forms import RegistrationForm, LoginForm

auth = Blueprint("auth", __name__)

@auth.route("/auth/register")
def register():
  form = RegistrationForm()
  
  if form.validate() and form.register.data:
    pass
  
  return render_template("auth/register.html", form=form, title="Register")

@auth.route("/auth/login")
def login():
  form = LoginForm()
  
  if form.validate() and form.login.data:
    pass
  
  return render_template("auth/login.html", form=form, title="Login")