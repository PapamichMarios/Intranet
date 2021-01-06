from flask import request
from app import app
from flask_accepts import accepts, responds

from model.user import User
from schema.user_schema import UserSchema
from flask.wrappers import Response

from service.auth import UserService


@app.route('/register', methods=['POST'])
@accepts(schema=UserSchema)
@responds(schema=UserSchema)
def register() -> User:
    return UserService.create(request.parsed_obj)
