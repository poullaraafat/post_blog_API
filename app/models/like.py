from app import db


class Like(db.Model):
    """Model to represent likes on a post."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    # Unique constraint to ensure no duplicate likes
    __table_args__ = (db.UniqueConstraint('user_id', 'post_id', name='unique_user_post_like'),)

    def __repr__(self):
        """Return a string representation of the like."""
        return f"Like(user_id={self.user_id}, post_id={self.post_id})"
