from app import db
from model.movie import Movie
from schema.movie import MovieSchema


class MovieService:

    @staticmethod
    def create(movie: Movie) -> dict:
        new_movie = Movie(
            name=movie['name'],
            description=movie['description'],
            year=movie['year'],
            duration=movie['duration'],
            genres=movie['genres'])

        db.session.add(new_movie)
        db.session.commit()

        return MovieSchema().dump(new_movie)

    @staticmethod
    def get_all() -> dict:
        return MovieSchema().dump(Movie.query.all())

    @staticmethod
    def get_by_id(movie_id: int) -> dict:
        return MovieSchema().dump(Movie.query.filter(Movie.id == movie_id).first())
