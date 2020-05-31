from flask_jwt import JWT, jwt_required, current_identity
from app.model.User import User
from werkzeug.security import safe_str_cmp

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    _id = payload['identity']
    return User.query.get(_id, None)


def configure(app):
    return JWT(app, authenticate, identity)