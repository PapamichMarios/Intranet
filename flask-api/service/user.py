from sqlalchemy import or_

from app import db, bcrypt
from enums.role import RoleEnum
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
            country=new_user['country'],
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
