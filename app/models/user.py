from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """User model for storing user-related details."""
    # Defining the fields for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_picture = db.Column(db.String(20), default=None)

    # One-to-many relationship with posts
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password):
        """Initialize a new user with username, email, and password."""
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches the hashed password in the database."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        """Return a string representation of the user."""
        return f"User('{self.username}', '{self.email}', '{self.profile_picture}')"
