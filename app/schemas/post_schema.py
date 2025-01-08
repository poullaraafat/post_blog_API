from marshmallow import Schema, fields


class PostSchema(Schema):
    """Schema for serializing and deserializing Post objects."""
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, error_messages={"required": "Title is required."})
    content = fields.Str(required=True, error_messages={"required": "Content is required."})
    date_posted = fields.DateTime(dump_only=True)
    user_id = fields.Int(dump_only=True)
    author = fields.Method("get_author", dump_only=True)

    # Nested fields
    comments = fields.Nested('CommentSchema', many=True,
                             only=('id', 'content', 'created_at'), dump_only=True)
    tags = fields.Nested('TagSchema', many=True, only=('name',), dump_only=True)
    likes = fields.Method("get_likes_count", dump_only=True)

    def get_likes_count(self, post):
        """Return the number of likes for a post."""
        return len(post.likes) if post.likes else 0

    def get_author(self, post):
        """Return the username of the post's author."""
        return post.author.username
    
    def get_likes_count(self, post):
        """Return the number of likes for a post."""
        return len(post.likes) if post.likes else 0



# Single and multiple post schemas
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
