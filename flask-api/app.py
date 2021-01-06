from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import JWTManager


# Configuration
app = Flask(__name__)

# Bcrypt
bcrypt = Bcrypt(app)

# JWT
app.config['JWT_SECRET_KEY'] = "Int|R@n3T"
jwt = JWTManager(app)

# SQL Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/intranet"
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# import models, controllers, error handlers
import model.user
import controller.auth
import error_handler

Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    app.run()
