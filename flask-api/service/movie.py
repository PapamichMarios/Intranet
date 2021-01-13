from app import db
from exception.movie_exists import MovieExists
from exception.resource_not_found import ResourceNotFound
from model.genre import Genre
from model.movie import Movie
from model.rating import Rating
from model.role import Role
from model.user import User
from schema.genre import GenreSchema
from schema.movie import MovieSchema
from schema.rating_movie import RatingMovieSchema
from schema.rating_movie_id import RatingMovieIdSchema


class MovieService:

    @staticmethod
    def create(movie: Movie) -> dict:

        db_movie = Movie.query.filter(Movie.name == movie['name'])
        if db_movie:
            raise MovieExists("Movie already exists")

        new_movie = Movie(
            name=movie['name'],
            description=movie['description'],
            year=movie['year'],
            duration=movie['duration'])

        for genre in movie['genres']:
            new_movie.genres.append(Genre.query.get(genre['id']))

        db.session.add(new_movie)
        db.session.commit()

        return MovieSchema().dump(new_movie)

    @staticmethod
    def get_all() -> dict:
        return MovieSchema(many=True).dump(
            Movie.query.all())

    @staticmethod
    def get_all_by_genre(genre_name) -> dict:
        return MovieSchema(many=True).dump(
            Movie.query.join(Movie.genres).filter(Genre.name == genre_name).all())

    @staticmethod
    def get_by_id(movie_id: int, username: str) -> dict:
        movie = Movie.query.get(movie_id)
        if not movie:
            raise ResourceNotFound("Movie not found")

        has_rated = MovieService.has_rated(username, movie)
        return {
            "movie": MovieSchema().dump(movie),
            "hasRated": has_rated
        }

    @staticmethod
    def search_by_name(name: str) -> dict:
        search = "%{}%".format(name)
        return MovieSchema(many=True).dump(
            Movie.query.filter(Movie.name.ilike(search)).all())

    @staticmethod
    def has_rated(username: str, movie: Movie) -> bool:
        user = User.query.filter(User.username == username).first()
        if not user:
            return False

        has_rated = False
        for rating in movie.ratings:
            if rating.user_id == user.id:
                has_rated = True

        return has_rated

    @staticmethod
    def rate_movie(username: str, rating: RatingMovieIdSchema) -> dict:
        user = User.query.filter(User.username == username).first()
        if not user:
            raise ResourceNotFound("User not found")

        movie = Movie.query.get(rating['movie_id'])
        if not movie:
            raise ResourceNotFound("Movie not found")

        new_rating = Rating(rating=rating['rating'], comment=rating['comment'])
        new_rating.movie_id = movie.id
        new_rating.user_id = user.id

        db.session.add(new_rating)
        db.session.commit()

        return RatingMovieIdSchema().dump(new_rating)

