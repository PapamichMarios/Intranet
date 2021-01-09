from marshmallow import Schema, fields, validate

from schema.genre import GenreSchema
from schema.rating import RatingSchema


class MovieSchema(Schema):
    id = fields.Number(attribute="id")
    name = fields.String(attribute="name", validate=validate.Length(min=3, max=256), required=True)
    description = fields.String(attribute="description", validate=validate.Length(min=3, max=256), required=True)
    year = fields.Integer(attribute="year", required=True)
    duration = fields.Integer(attribute="duration", required=True)
    ratings = fields.Nested(RatingSchema, many=True)
    genres = fields.Nested(GenreSchema, many=True)
