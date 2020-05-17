from app.config.database import db
from app.model import User
from app.model import Post

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True) 
    comment = db.Column(db.String(255), nullable=False) 
    created_at = db.Column(db.String(50)) 
    updated_at = db.Column(db.String(100)) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
