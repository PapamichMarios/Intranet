from sqlalchemy import Column, Integer, String, Date
from app import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    first_name = Column(String)
    last_name = Column(String)
    country = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
