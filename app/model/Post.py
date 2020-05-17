from app.config.database import db
from app.model import Comment

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    author = db.Column(db.String(255))
    is_active = db.Column(db.Boolean(), default=True)
    comment = db.relationship('Comment', backref="post")
