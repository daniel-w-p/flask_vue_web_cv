from .ma_init import MA

ma = MA.get()


class UserSchema(ma.Schema):
    """
    User schema
    """

    class Meta:
        fields = ("id", "username", "email", "password")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
