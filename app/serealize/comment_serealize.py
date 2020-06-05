from app.config.serealize import ma
from app.model.Comment import Comment

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'created_at', 'updated_at', 'user_id', 'post_id')
        ordered = True
        load_instance = True
