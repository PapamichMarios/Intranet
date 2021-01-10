from app import db
import model.movie, model.user


class Rating(db.Model):
    __tablename__ = "rating"
    id = db.Column('rating_id', db.Integer, primary_key=True, index=True, autoincrement=True)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
