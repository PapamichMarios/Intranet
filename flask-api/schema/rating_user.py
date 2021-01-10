from marshmallow import Schema, fields

from schema.user import UserSchema


class RatingUserSchema(Schema):
    id = fields.Number(attribute="id")
    rating = fields.Float(attribute="rating", required=True)
    comment = fields.String(attribute="comment", required=False)
    user = fields.Nested(UserSchema)
