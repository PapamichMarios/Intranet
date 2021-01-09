from sqlalchemy import or_

from app import db, bcrypt
from enums.role import RoleEnum
from exception.resource_not_found import ResourceNotFound
from exception.username_email_exists import UsernameEmailExists
from model.role import Role
from model.user import User
from schema.user import UserSchema
from service.role import RoleService


class UserService:

    @staticmethod
    def create(new_user: User) -> dict:
        # check if email or username exists
        user_db = User.query.filter(or_(User.username == new_user['username'], User.email == new_user['email'])).first()

        if user_db:
            raise UsernameEmailExists('Username or email already exists!')

        roles = [RoleService.find_by_role(RoleEnum.ROLE_USER.name)]
        user_to_save = User(
            first_name=new_user['first_name'],
            last_name=new_user['last_name'],
            email=new_user['email'],
            username=new_user['username'],
            # hash password
            password=bcrypt.generate_password_hash(new_user['password']).decode('utf-8'),
            roles=roles)

        db.session.add(user_to_save)
        db.session.commit()

        return UserSchema().dump(user_to_save)

    @staticmethod
    def get_all() -> dict:
        return UserSchema().dump(User.query.all())

    @staticmethod
    def my_profile(username: str) -> dict:
        profile = User.query.filter(User.username == username).first()
        if not profile:
            raise ResourceNotFound('User not found')

        return UserSchema().dump(profile)

    @staticmethod
    def update_profile(user: User) -> dict:
        db_user = User.query.filter(User.id == user['id'])
        if not db_user:
            raise ResourceNotFound('User not found')

        db_user.username = user['username']
        db_user.first_name = user['first_name']
        db_user.last_name = user['last_name']
        db_user.email = user['email']
        db_user.roles = user['roles']

        db.session.commit()
        return UserSchema().dump(db_user)