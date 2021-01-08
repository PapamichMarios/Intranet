from marshmallow import Schema, fields

from schema.movie import MovieSchema
from schema.user import UserSchema


class RatingSchema(Schema):
    id = fields.Number(attribute="id")
    rating = fields.Float(attribute="rating", required=True)
    movie = fields.Nested(MovieSchema)
    user = fields.Nested(UserSchema)
