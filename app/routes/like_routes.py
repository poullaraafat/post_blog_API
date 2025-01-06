from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Post, User, Like
from app import db
from app.schemas.post_schema import post_schema

# Create a Blueprint for like routes
like = Blueprint('like', __name__)

@like.route('/posts/<int:post_id>/like', methods=['POST'])
@jwt_required()
def like_post(post_id):
    # Get the current user's ID from the JWT token
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    # Check if the user has already liked the post
    like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
    if like:
        return jsonify({'message': 'You have already liked this post'}), 400

    # Create a new like
    like = Like(user_id=user_id, post_id=post_id)
    db.session.add(like)
    db.session.commit()

    return jsonify({
        'message': 'Post liked successfully',
        'data': post_schema.dump(post),
        "likes": len(post.likes)
    }), 200

@like.route('/posts/<int:post_id>/unlike', methods=['POST'])
@jwt_required()
def unlike_post(post_id):
    # Get the current user's ID from the JWT token
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    # Check if the user has liked the post
    like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
    if not like:
        return jsonify({'message': 'You have not liked this post'}), 400

    # Remove the like
    db.session.delete(like)
    db.session.commit()

    return jsonify({
        'message': 'Post unliked successfully',
        'data': post_schema.dump(post),
        "likes": len(post.likes)
    }), 200
