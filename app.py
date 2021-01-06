from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import JWTManager


# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/intranet"
app.config['JWT_SECRET_KEY'] = "Int|R@n3T"

# Bcrypt
bcrypt = Bcrypt(app)

# JWT
jwt = JWTManager(app)

# SQL Alchemy
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# import models, controllers, error handlers
import model.user
import controller.auth
import error

Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    app.run()
