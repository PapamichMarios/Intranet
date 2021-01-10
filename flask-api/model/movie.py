from app import db
import model.genre

movie_genres_table = db.Table('movie_has_genres', db.Model.metadata,
                              db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id'), primary_key=True),
                              db.Column('genre_id', db.Integer, db.ForeignKey('genre.genre_id')), primary_key=True)


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column('movie_id', db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    ratings = db.relationship('Rating', backref='movie', lazy=True)
    genres = db.relationship('Genre', secondary=movie_genres_table)
