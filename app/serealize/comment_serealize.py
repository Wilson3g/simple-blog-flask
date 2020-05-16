from app.config.serealize import ma

class CommentSchema(ma.Schema):
    class Meta:
        fields = ('comment', 'created_at', 'updated_at', 'user_id')