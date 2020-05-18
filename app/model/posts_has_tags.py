from app.config.database import db
from app.model import Tags
from app.model import Post

class PostHasTags(db.Model):
    __tablename__ = 'posts_has_tags'
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    post = db.relationship('Post', backref='tag_assoc')
    tag = db.relationship('Tags.Tag', backref='post_assoc')