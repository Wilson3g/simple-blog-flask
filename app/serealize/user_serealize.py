from app.config.serealize import ma
from app.model.User import User
from flask_marshmallow import fields

# Serealization class
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_admin', 'password')
        ordered = True
        load_instance = True
