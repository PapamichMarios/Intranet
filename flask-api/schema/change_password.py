from marshmallow import Schema, fields, validate


class ChangePasswordSchema(Schema):
    id = fields.Number(attribute="id")
    oldPassword = fields.String(attribute="old_password", validate=validate.Length(min=8, max=256), required=True)
    password = fields.String(attribute="password", validate=validate.Length(min=8, max=256), required=True)
