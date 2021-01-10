from marshmallow import Schema, fields


class RatingSchema(Schema):
    id = fields.Number(attribute="id")
    rating = fields.Float(attribute="rating", required=True)
    comment = fields.String(attribute="commend", required=False)
