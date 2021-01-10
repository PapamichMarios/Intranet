from flask import request
from flask_accepts import responds, accepts
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_optional

from app import app
from model.response import ApiResponse
from schema.movie import MovieSchema
from schema.rating_movie import RatingMovieSchema
from schema.rating_movie_id import RatingMovieIdSchema
from schema.response import ApiResponseSchema
from service.auth import AuthService
from service.genre import GenreService
from service.movie import MovieService


@app.route('/movies/all', methods=['GET'])
@responds(schema=ApiResponseSchema)
def get_all_movies() -> ApiResponse:
    return ApiResponse(MovieService.get_all(), True)


@app.route('/movies/create', methods=['POST'])
@jwt_required
@accepts(schema=MovieSchema)
@responds(schema=ApiResponseSchema)
def create_movie() -> ApiResponse:
    AuthService.is_admin()
    return ApiResponse(MovieService.create(request.parsed_obj), True)


@app.route('/movies/all/genre/<genre_name>', methods=['GET'])
@responds(schema=ApiResponseSchema)
def get_all_movies_by_genre(genre_name) -> ApiResponse:
    return ApiResponse(MovieService.get_all_by_genre(genre_name), True)


@app.route('/movies/<int:movie_id>', methods=['GET'])
@jwt_optional
@responds(schema=ApiResponseSchema)
def get_movie_by_id_logged_in(movie_id) -> ApiResponse:
    return ApiResponse(MovieService.get_by_id(movie_id, get_jwt_identity()), True)


@app.route('/movies/search', methods=['GET'])
@responds(schema=ApiResponseSchema)
def search():
    return ApiResponse(MovieService.search_by_name(request.args.get('name')), True)


@app.route('/movies/genres', methods=['GET'])
@responds(schema=ApiResponseSchema)
def movie_genres():
    return ApiResponse(GenreService.get_movie_genres_all(), True)


@app.route('/movies/rate', methods=['POST'])
@jwt_required
@accepts(schema=RatingMovieIdSchema)
@responds(schema=ApiResponseSchema)
def rate_movie() -> ApiResponse:
    return ApiResponse(MovieService.rate_movie(get_jwt_identity(), request.parsed_obj), True)
