from flask import request
from flask_accepts import responds
from flask_jwt_extended import jwt_required

from app import app
from model.response import ApiResponse
from schema.response import ApiResponseSchema
from service.auth import AuthService
from service.genre import GenreService
from service.movie import MovieService


@app.route('/movies/all', methods=['GET'])
@responds(schema=ApiResponseSchema)
def get_all_movies() -> ApiResponse:
    return ApiResponse(MovieService.get_all(), True)


@app.route('/movies/all/genre/<genre_name>', methods=['GET'])
@responds(schema=ApiResponseSchema)
def get_all_movies_by_genre(genre_name) -> ApiResponse:
    return ApiResponse(MovieService.get_all_by_genre(genre_name), True)


@app.route('/movies/<int:movie_id>', methods=['GET'])
@jwt_required
@responds(schema=ApiResponseSchema)
def get_movie_by_id(movie_id) -> ApiResponse:
    return ApiResponse(MovieService.get_by_id(movie_id), True)


@app.route('/movies/search', methods=['GET'])
@responds(schema=ApiResponseSchema)
def search():
    return ApiResponse(MovieService.search_by_name(request.args.get('name')), True)


@app.route('/movies/genres', methods=['GET'])
@responds(schema=ApiResponseSchema)
def movie_genres():
    return ApiResponse(GenreService.get_movie_genres_all(), True)
