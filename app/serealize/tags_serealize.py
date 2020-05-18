from app.config.serealize import ma

class TagSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'is_active')