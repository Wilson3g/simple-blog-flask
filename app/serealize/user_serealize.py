from app.config.serealize import ma

# Serealization class
class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'username', 'password')