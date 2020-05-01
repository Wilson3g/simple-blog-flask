# Serealizing imports
from flask_marshmallow import Marshmallow, Schema
from ..model.Model import User, Comment

# Serealizations
ma = Marshmallow()

def configure(app):
    ma.init_app(app)

# Serealization class
class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'username', 'password')

class CommentSchema(ma.Schema):
    class Meta:
        fields = ('comment', 'created_at', 'updated_at', 'user_id')