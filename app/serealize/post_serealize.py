from app.config.serealize import ma

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'author')