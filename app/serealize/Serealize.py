from app.config.serealize import ma

# Serealization class
class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'username', 'password')

class CommentSchema(ma.Schema):
    class Meta:
        fields = ('comment', 'created_at', 'updated_at', 'user_id')