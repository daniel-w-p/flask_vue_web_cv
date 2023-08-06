from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


class DB:
    """
    DB connection
    """
    __db = SQLAlchemy()
    __bcrypt = Bcrypt()

    @classmethod
    def set(cls, app, credentials):
        """
        Set flask app
        :param app: Flask
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(credentials.username,
                                                                                     credentials.password,
                                                                                     credentials.host,
                                                                                     credentials.port,
                                                                                     credentials.database)
        cls.__db.init_app(app)
        cls.__bcrypt.init_app(app)

    @classmethod
    def get(cls):
        return cls.__db

    @classmethod
    def bcrypt(cls):
        return cls.__bcrypt

