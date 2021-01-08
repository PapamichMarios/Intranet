from marshmallow import Schema, fields, validate


class GenreSchema(Schema):
    id = fields.Number(attribute="id")
    name = fields.String(attribute="name", validate=validate.Length(min=3, max=256), required=True)
    description = fields.String(attribute="description", validate=validate.Length(min=3, max=256), required=True)
