from marshmallow import Schema, fields


class UserSchema(Schema):
    """Schema for serializing and deserializing User objects."""
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, error_messages={"required": "Username is required."})
    email = fields.Email(required=True, error_messages={"required": "Email is required."})
    profile_picture = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    posts = fields.Nested('PostSchema', many=True,
                          only=('id', 'title', 'date_posted'), dump_only=True)


# Single and multiple user schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)


class LoginSchema(Schema):
    email = fields.Email(required=True, error_messages={"required": "Email is required."})
    password = fields.Str(required=True, error_messages={"required": "Password is required."})

login_schema = LoginSchema()
