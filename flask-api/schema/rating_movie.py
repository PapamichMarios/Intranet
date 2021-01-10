from marshmallow import Schema, fields

from schema.movie import MovieSchema


class RatingMovieSchema(Schema):
    id = fields.Number(attribute="id")
    rating = fields.Float(attribute="rating", required=True)
    comment = fields.String(attribute="comment", required=False)
    movie = fields.Nested(MovieSchema)
