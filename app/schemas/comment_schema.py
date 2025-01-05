from marshmallow import Schema, fields, validate


class CommentSchema(Schema):
    """Schema for serializing and deserializing Comment objects."""
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True, validate=validate.Length(min=1),
                         error_messages={"required": "Content is required."})
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user_id = fields.Int(dump_only=True)
    post_id = fields.Int(dump_only=True)

    # Nested fields
    user = fields.Nested('UserSchema', only=('id', 'username'), dump_only=True)
    post = fields.Nested('PostSchema', only=('id', 'title'), dump_only=True)


# Single and multiple comment schemas
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
