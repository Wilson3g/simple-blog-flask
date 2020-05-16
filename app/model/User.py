from app.config.database import db
from app.model import Comment

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), nullable=False, unique=True) 
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    comment = db.relationship('Comment', backref="user")
    is_admin = db.Column(db.Boolean())