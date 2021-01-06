import bcrypt as bcrypt
from sqlalchemy import Column, Integer, String, Date
from app import Base, app


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    country = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)

    def __init__(self, first_name, last_name, country, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS'))
