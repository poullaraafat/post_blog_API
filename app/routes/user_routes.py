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


