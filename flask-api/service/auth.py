from flask_jwt_extended import create_access_token

from app import db, bcrypt
from exception.bad_credentials import BadCredentials
from exception.resource_not_found import ResourceNotFound
from model.user import User
from schema.login import LoginSchema
from schema.user import UserSchema
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

    @staticmethod
    def my_profile(username: str) -> dict:
        profile = User.query.filter(User.username == username).first()
        if not profile:
            raise ResourceNotFound('Username not found')

        return UserSchema().dump(profile)
