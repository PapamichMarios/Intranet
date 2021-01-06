from sqlalchemy import or_
from app import Session, app, bcrypt
from exception.username_email_exists import UsernameEmailExists
from model.user import User


class UserService:

    @staticmethod
    def create(new_user: User) -> User:
        # check if email or username exists
        session = Session()
        user_db = session.query(User).filter(
            or_(User.username == new_user['username'], User.email == new_user['email'])).first()

        if user_db:
            raise UsernameEmailExists('Username or email already exists!')

        # hash password
        user_to_save = User(
            new_user['first_name'],
            new_user['last_name'],
            new_user['country'],
            new_user['email'],
            new_user['username'],
            new_user['password']
        )
        session.add(user_to_save)
        session.commit()

        return new_user
