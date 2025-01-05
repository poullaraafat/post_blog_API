from app import db


# Association table for the many-to-many relationship between posts and tags
post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Tag(db.Model):
    """Tag model for storing tag-related details."""
    # Defining the fields for the Tag model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    # Many-to-many relationship with posts through the association table
    posts = db.relationship('Post', secondary=post_tags, backref=db.backref('tags', lazy='dynamic'))

    def __repr__(self):
        """Return a string representation of the tag."""
        return f"Tag(id={self.id}, name='{self.name}')"
