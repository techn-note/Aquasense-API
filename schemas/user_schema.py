from marshmallow import Schema, fields, validate, validates, ValidationError
from models.user import User

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    age = fields.Int(required=True, validate=validate.Range(min=0))
    country = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))
    created_at = fields.DateTime(dump_only=True)

    @validates('email')
    def validate_unique_email(self, email):
        if User.get_user_by_email(email):
            raise ValidationError('Email already exists.')
