from marshmallow import Schema, fields, validate


class ApiResponseSchema(Schema):
    data = fields.Raw(required=True)
    success = fields.Boolean(required=True)
