from app.config.database import db
from app.model import Comment
from app.model.Tags import Tag
from app.model import posts_has_tags

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    author = db.Column(db.String(255))
    is_active = db.Column(db.Boolean(), default=True)
    comment = db.relationship('Comment', backref="post")
    tags = db.relationship('Tag', secondary='posts_has_tags')
