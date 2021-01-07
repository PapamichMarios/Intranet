from flask_jwt_extended import create_access_token

from app import db, bcrypt
from exception.bad_credentials import BadCredentials
from model.user import User
from schema.login import LoginSchema
from service.user import UserService


class AuthService:

    @staticmethod
    def register(new_user: User) -> dict:
        return UserService.create(new_user)


    @staticmethod
    def authenticate(credentials: LoginSchema) -> dict:

        user = User.query.filter(User.username == credentials['username']).first()
        db.session.commit()

        if not user:
            raise BadCredentials('Wrong username or password.')

        if not bcrypt.check_password_hash(user.password, credentials['password']):
            raise BadCredentials('Wrong Username or password.')

        return {'jwt': create_access_token(identity=credentials['username'])}