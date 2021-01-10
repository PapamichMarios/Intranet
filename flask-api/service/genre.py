from model.genre import Genre
from schema.genre import GenreSchema


class GenreService:

    @staticmethod
    def get_movie_genres_all() -> dict:
        return GenreSchema(many=True).dump(
            Genre.query.all()
        )
