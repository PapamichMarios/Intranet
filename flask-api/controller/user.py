from flask_accepts import responds, accepts
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from app import app
from model.response import ApiResponse
from schema.response import ApiResponseSchema
from schema.user import UserSchema
from service.auth import AuthService
from service.user import UserService


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
    return ApiResponse(UserService.update_profile(request.parsed_obj))