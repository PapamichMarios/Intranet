from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from app import app
from flask_accepts import accepts, responds
from model.response import ApiResponse
from schema.login import LoginSchema
from schema.response import ApiResponseSchema
from schema.user import UserSchema
from service.auth import AuthService


@app.route('/register', methods=['POST'])
@accepts(schema=UserSchema)
@responds(schema=ApiResponseSchema)
def register() -> ApiResponse:
    return ApiResponse(AuthService.register(request.parsed_obj), True)


@app.route('/login', methods=['POST'])
@accepts(schema=LoginSchema)
@responds(schema=ApiResponseSchema)
def login() -> ApiResponse:
    return ApiResponse(AuthService.authenticate(request.parsed_obj), True)


@app.route('/protected', methods=['GET'])
@jwt_required
@responds(schema=ApiResponseSchema)
def protected() -> ApiResponse:
    current_user = get_jwt_identity()
    return ApiResponse(current_user, True)