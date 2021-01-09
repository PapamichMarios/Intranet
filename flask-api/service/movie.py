from app import db
from model.genre import Genre
from model.movie import Movie
from model.role import Role
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
        return MovieSchema(many=True).dump(Movie.query.all())

    @staticmethod
    def get_all_by_genre(genre_id) -> dict:
        return MovieSchema(many=True).dump(
            Movie.query.join(Movie.genres).filter(Genre.id == genre_id).all())

    @staticmethod
    def get_by_id(movie_id: int) -> dict:
        return MovieSchema().dump(Movie.query.get(movie_id))

    @staticmethod
    def search_by_name(name: str) -> dict:
        search = "%{}%".format(name)
        movies = Movie.query.filter(Movie.name.ilike(search)).all()
        print(movies)
        return MovieSchema(many=True).dump(movies)
