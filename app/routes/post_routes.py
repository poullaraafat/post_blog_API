from flask import Blueprint, request, jsonify
from app.models import Post, User
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.schemas.post_schema import post_schema
from marshmallow import ValidationError

post = Blueprint('post', __name__)

@post.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)

    data = request.get_json()

    try:
        post_schema.load(data)
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 400

    new_post = Post(title=data['title'], content=data['content'], user_id=user_id)

    db.session.add(new_post)
    db.session.commit()

    return jsonify({
            'message': 'Post created successfully',
            'data': post_schema.dump(new_post)
    }), 201

@post.route('/posts/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    if int(post.user_id) != int(user_id):
        return jsonify({'message': 'You are not authorized to update this post'}), 403

    data = request.get_json()

    # Validate input data
    try:
        post_schema.load(data, partial=True)  # Use partial=True to allow partial updates
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 400

    # Update the post fields
    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']

    db.session.commit()
    
    return jsonify({
            'message': 'Post updated successfully',
            'data': post_schema.dump(post)
    }), 200

@post.route('/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    # Ensure the user is the author of the post
    if int(post.user_id) != int(user_id):
        return jsonify({'message': 'You are not authorized to delete this post'}), 403

    # Delete the post
    db.session.delete(post)
    db.session.commit()

    return jsonify({
        'message': 'Post deleted successfully'
    }), 200
