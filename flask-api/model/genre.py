from app import db


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column('genre_id', db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)