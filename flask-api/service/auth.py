from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.exceptions import Unauthorized

from app import db, bcrypt
from enums.role import RoleEnum
from exception.bad_credentials import BadCredentials
from exception.resource_not_found import ResourceNotFound
from model.user import User
from schema.login import LoginSchema
from schema.role import RoleSchema
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

        return {
            "auth": {
                "type": "Bearer ",
                "token": create_access_token(identity=credentials['username'], expires_delta=False)
            },
            "roles": RoleSchema(many=True).dump(user.roles)
        }

    @staticmethod
    def is_admin():
        username = get_jwt_identity()
        user = User.query.filter(User.username == username).first()
        role = list(filter(lambda x: x.name == RoleEnum.ROLE_ADMINISTRATOR.name, user.roles))
        if not role:
            raise Unauthorized
