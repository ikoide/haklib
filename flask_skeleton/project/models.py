from datetime import datetime
from project import db, login_manager
from flask_login import UserMixin, current_user

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(16), unique=True, nullable=False)
  email = db.Column(db.String(64), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=False)
  
  join_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
