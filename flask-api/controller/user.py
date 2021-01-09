from flask_accepts import responds, accepts
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from werkzeug.exceptions import Unauthorized

from app import app
from enums.role import RoleEnum
from model.response import ApiResponse
from model.user import User
from schema.change_password import ChangePasswordSchema
from schema.response import ApiResponseSchema
from schema.user import UserSchema
from service.auth import AuthService
from service.user import UserService


@app.route('/users/all', methods=['GET'])
@jwt_required
@responds(schema=ApiResponseSchema)
def get_all_users() -> ApiResponse:
    AuthService.is_admin()
    return ApiResponse(UserService.get_all(), True)


@app.route('/profile', methods=['GET'])
@jwt_required
@responds(schema=ApiResponseSchema)
def profile() -> ApiResponse:
    return ApiResponse(UserService.my_profile(get_jwt_identity()), True)


@app.route('/profile', methods=['PUT'])
@jwt_required
@accepts(schema=UserSchema)
@responds(schema=ApiResponseSchema)
def update_profile() -> ApiResponse:
    return ApiResponse(UserService.update_profile(request.parsed_obj), True)


@app.route('/change_password', methods=['PUT'])
@jwt_required
@accepts(schema=ChangePasswordSchema)
@responds(schema=ApiResponseSchema)
def change_password() -> ApiResponse:
    return ApiResponse(UserService.change_password(request.parsed_obj['id'],
                                                   request.parsed_obj['old_password'],
                                                   request.parsed_obj['password']), True)
