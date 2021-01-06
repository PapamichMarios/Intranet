from sqlalchemy import Column, Integer, String
from app import Base, app, bcrypt


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    country = Column(String)
    email = Column(String)

    def __init__(self, first_name, last_name, country, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
