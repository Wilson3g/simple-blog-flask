from app.config.serealize import ma
from app.model.Post import Post
from flask_marshmallow import fields


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author')
        ordered = True
        load_instance = True
