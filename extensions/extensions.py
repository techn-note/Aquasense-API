from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class Extensions:

    @staticmethod
    def initialize_jwt(app):
        JWTManager(app)

    @staticmethod
    def initialize_marsh(app):
        marsh = Marshmallow()
        marsh.init_app(app)

    @staticmethod
    def initialize_bcript(app):
        bcrypt.init_app(app)
