from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), nullable=False, unique=True) 
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    comment = db.relationship('comment')
    # is_admin = db.Column(db.String(10))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        # self.is_admin = is_admin


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    comment = db.Column(db.String(255), nullable=False) 
    created_at = db.Column(db.String(50)) 
    updated_at = db.Column(db.String(100)) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    def __init__(self, comment, created_at, updated_at, user_id):
        self.comment = comment
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_id = user_id