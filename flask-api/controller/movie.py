from flask import request
from flask_accepts import responds
from flask_jwt_extended import jwt_required

from app import app
from model.response import ApiResponse
from schema.response import ApiResponseSchema
from service.auth import AuthService
from service.movie import MovieService


@app.route('/movies/all', methods=['GET'])
@jwt_required
@responds(schema=ApiResponseSchema)
def get_all_movies() -> ApiResponse:
    AuthService.is_admin()
    return ApiResponse(MovieService.get_all(), True)


@app.route('/movies/<int:movie_id>', methods=['GET'])
@jwt_required
@responds(schema=ApiResponseSchema)
def get_movie_by_id(movie_id) -> ApiResponse:
    AuthService.is_admin()
    return ApiResponse(MovieService.get_by_id(movie_id), True)


@app.route('/search', methods=['GET'])
@responds(schema=ApiResponseSchema)
def search():
    return ApiResponse(MovieService.search_by_name(request.args.get('name')), True)
