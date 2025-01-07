from marshmallow import Schema, fields, validate, ValidationError


class UserSchema(Schema):
    """Schema for serializing and deserializing User objects."""
    id = fields.Int(dump_only=True)
    username = fields.Str(
        required=True,
        error_messages={"required": "Username is required."},
        validate=validate.Length(
            min=8, max=32,
            error="Username must be between 8 and 32 characters long."
        )
    )
    email = fields.Email(
        required=True,
        error_messages={"required": "Email is required."}
    )
    password = fields.Str(
        required=True,
        load_only=True,
        error_messages={"required": "Password is required."},
        validate=validate.Length(
            min=8, max=32,
            error="Password must be between 8 and 32 characters long."
        )
    )
    created_at = fields.DateTime(dump_only=True)
    posts = fields.Nested(
        'PostSchema', many=True,
        only=('id', 'title', 'date_posted'), dump_only=True
    )


# Single and multiple user schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)


class LoginSchema(Schema):
    """Schema for validating login credentials."""
    email = fields.Email(
        required=True,
        error_messages={"required": "Email is required."}
    )
    password = fields.Str(
        required=True,
        error_messages={"required": "Password is required."}
    )


login_schema = LoginSchema()
