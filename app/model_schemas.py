from app import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'password', 'name')


class TextSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'provider', 'count')


user_schema = UserSchema()
user_schema = UserSchema(many=True)

text_schema = TextSchema()
text_schema = TextSchema(many=True)
