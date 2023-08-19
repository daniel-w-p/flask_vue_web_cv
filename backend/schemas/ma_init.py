from flask_marshmallow import Marshmallow


class MA:
    """ Marshmallow serialization"""
    __ma = Marshmallow()

    @classmethod
    def set(cls, app):
        """
        Set the app
        :param app: Flask
        """
        cls.__ma.init_app(app)

    @classmethod
    def get(cls):
        """
        Get __ma
        :return: Marshmallow instance
        """
        return cls.__ma
