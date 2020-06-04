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

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def check_email_exists(cls, email: str):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def search_by_id(cls, id: int):
        return cls.query.get(id)

    @classmethod
    def show_all_users(cls):
        return cls.query.all()
