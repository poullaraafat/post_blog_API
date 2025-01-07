from datetime import datetime
from app import db


class Post(db.Model):
    """Post model for storing post-related details."""
    # Defining the fields for the Post model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # One-to-many relationship: each post has many comments
    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")

    # One-to-many relationship: each post can have many likes
    likes = db.relationship('Like', backref='post', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        """Return a string representation of the post."""
        return f"Post('{self.title}', '{self.date_posted}')"
