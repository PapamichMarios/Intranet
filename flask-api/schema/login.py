from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    username = fields.String(attribute="username", validate=validate.Length(min=3, max=256), required=True)
    password = fields.String(attribute="password", validate=validate.Length(min=8, max=256), required=True)
