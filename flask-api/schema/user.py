from marshmallow import Schema, fields, validate

from schema.rating import RatingSchema
from schema.rating_movie import RatingMovieSchema
from schema.role import RoleSchema


class UserSchema(Schema):
    id = fields.Number(attribute="id")
    firstName = fields.String(attribute="first_name", validate=validate.Length(min=3, max=256), required=True)
    lastName = fields.String(attribute="last_name", validate=validate.Length(min=3, max=256), required=True)
    email = fields.Email(attribute="email", validate=validate.Length(min=3, max=256), required=True)
    username = fields.String(attribute="username", validate=validate.Length(min=3, max=256), required=True)
    password = fields.String(attribute="password", validate=validate.Length(min=8, max=256), required=True)
    roles = fields.Nested(RoleSchema, many=True)
    ratings = fields.Nested(RatingMovieSchema, many=True)
