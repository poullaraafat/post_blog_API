from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Comment, Post, User
from app import db
from app.schemas.comment_schema import comment_schema, comments_schema
from marshmallow import ValidationError

# Create a Blueprint for comment routes
comment = Blueprint('comment', __name__)

@comment.route('/posts/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def create_comment(post_id):
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    data = request.get_json()
    # Validate input data
    try:
        comment_schema.load(data)
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 400

    # Create a new comment
    comment = Comment(content=data['content'], user_id=user_id, post_id=post_id)
    db.session.add(comment)
    db.session.commit()

    return jsonify({
        'message': 'Comment created successfully',
        'data': comment_schema.dump(comment)
    }), 201

@comment.route('/comments/<int:comment_id>', methods=['PUT'])
@jwt_required()
def update_comment(comment_id):
    user_id = get_jwt_identity()
    comment = Comment.query.get_or_404(comment_id) 

    if int(comment.user_id) != int(user_id):
        return jsonify({'message': 'You are not authorized to update this comment'}), 403

    data = request.get_json()

    # Validate input data
    try:
        comment_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 400

    # Update the comment content if provided
    if 'content' in data:
        if not data['content']:
            return jsonify({'message': 'Comment content cannot be empty'}), 400
        comment.content = data['content']

    db.session.commit()

    return jsonify({
        'message': 'Comment updated successfully',
        'data': comment_schema.dump(comment)
    }), 200


@comment.route('/comments/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comment_id):
    # Get the current user's ID from the JWT token
    user_id = int(get_jwt_identity())  # Convert to integer
    comment = db.session.get(Comment, comment_id)  # Fetch the comment

    # Check if the comment exists
    if not comment:
        return jsonify({'message': 'Comment not found'}), 404

    # Check if the comment belongs to the authenticated user
    if int(comment.user_id) != int(user_id):
        return jsonify({'message': 'You are not authorized to delete this comment'}), 403

    db.session.delete(comment)
    db.session.commit()

    return jsonify({'message': 'Comment deleted successfully'}), 200

@comment.route('/posts/<int:post_id>/comments', methods=['GET'])
def get_comments_for_post(post_id):
    # Fetch the post to ensure it exists
    post = Post.query.get_or_404(post_id)

    # Fetch all comments associated with the post
    comments = Comment.query.filter_by(post_id=post_id).all()

    return jsonify({
        'message': 'Comments retrieved successfully',
        'data': comments_schema.dump(comments)
    }), 200
