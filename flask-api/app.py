from flask_bcrypt import Bcrypt
from flask import Flask
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

# Create roles
if not Role.query.all():
    admin_role = Role(id=1, name=RoleEnum.ROLE_ADMINISTRATOR.name, description='Admin Role')
    user_role = Role(id=2, name=RoleEnum.ROLE_USER.name, description='User Role')
    db.session.add(admin_role)
    db.session.add(user_role)
    db.session.commit()


if __name__ == '__main__':
    app.run()
