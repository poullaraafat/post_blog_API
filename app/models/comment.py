from datetime import datetime
from app import db

class Comment(db.Model):
    """Model to represent comments on a post."""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        """Return a string representation of the comment."""
        return f"Comment(id={self.id}, content='{self.content[:20]}...', user_id={self.user_id})"
