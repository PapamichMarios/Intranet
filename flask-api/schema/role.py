from marshmallow import fields, Schema


class RoleSchema(Schema):
    id = fields.Number(attribute="id")
    name = fields.String(required=True)
    description = fields.String()
