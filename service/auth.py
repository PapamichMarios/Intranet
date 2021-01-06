from flask_jwt_extended import create_access_token

from app import Session, bcrypt
from exception.bad_credentials import BadCredentials
from model.user import User
from schema.login import LoginSchema
from service.user import UserService


class AuthService:

    @staticmethod
    def register(new_user: User) -> User:
        return UserService.create(new_user)


    @staticmethod
    def authenticate(credentials: LoginSchema) -> dict:

        session = Session()
        user = session.query(User).filter(User.username == credentials['username']).first()
        session.commit()

        if not user:
            raise BadCredentials('Wrong username or password.')

        if not bcrypt.check_password_hash(user.password, credentials['password']):
            raise BadCredentials('Wrong Username or password.')

        return {'jwt': create_access_token(identity=credentials['username'])}