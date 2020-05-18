from app.config.database import db
from app.model import Post
from app.model import posts_has_tags

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    is_active = db.Column(db.Boolean(), default=True)
    posts = db.relationship('Post', secondary='posts_has_tags')
