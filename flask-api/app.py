from flask_bcrypt import Bcrypt
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

# Configuration
app = Flask(__name__)

# Bcrypt
bcrypt = Bcrypt(app)

# JWT
app.config['JWT_SECRET_KEY'] = "Int|R@n3T"
jwt = JWTManager(app)

# SQL Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/intranet"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from enums.role import RoleEnum
from model.role import Role
import controller.auth
import error_handler

db.create_all()

from service.configuration import ConfigurationService
ConfigurationService.init_db_data()

if __name__ == '__main__':
    app.run()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response