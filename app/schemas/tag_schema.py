from marshmallow import Schema, fields, validate

class TagSchema(Schema):
    """Schema for serializing and deserializing Tag objects."""
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=50),
        error_messages={"required": "The 'name' field is required."}
        )
    posts = fields.Nested('PostSchema', many=True, only=('id', 'title'), dump_only=True)

# Single and multiple tag schemas
tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
