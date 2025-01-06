from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from app import db
from app.schemas.user_schema import user_schema
from marshmallow import ValidationError

# Create a Blueprint for user routes
user = Blueprint('user', __name__)


@user.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Return the user's profile data
    return jsonify({
        'message': 'User profile retrieved successfully',
        'data': user_schema.dump(user)
    }), 200


@user.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id) 

    data = request.get_json()
    # Validate input data
    try:
        user_schema.load(data, partial=True)  # Allow partial updates
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 400

    # Check for field updates and apply them
    if 'username' in data and data['username'] != user.username:
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'The username is already taken. Please choose another.'}), 400
        user.username = data['username']

    # Update email (if provided and different)
    if 'email' in data and data['email'] != user.email:
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'The email is already registered. Please use another.'}), 400
        user.email = data['email']

    # Update profile picture (if provided)
    if 'profile_picture' in data:
        user.profile_picture = data['profile_picture']

    db.session.commit()

    return jsonify({
        'message': 'User profile updated successfully',
        'data': user_schema.dump(user)
    }), 200

