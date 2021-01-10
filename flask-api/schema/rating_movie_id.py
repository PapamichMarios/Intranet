from marshmallow import fields, Schema


class RatingMovieIdSchema(Schema):
    id = fields.Number(attribute="id")
    rating = fields.Float(attribute="rating", required=True)
    comment = fields.String(attribute="comment", required=False)
    movieId = fields.Integer(attribute="movie_id", required=True)
