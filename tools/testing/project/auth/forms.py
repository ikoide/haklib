from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from project.models import User

class RegistrationForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=4, max=16)])
  email = StringField("Email", validators=[DataRequired(), Length(min=8, max=64)])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=128)])
  confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
  register = SubmitField("Sign Up")
  
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError("That username is taken. Please choose a different one.")
    
class LoginForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  remember_me = BooleanField("Remember Me")
  login = SubmitField("Login")