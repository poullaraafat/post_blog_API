from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from flask_jwt_extended import create_access_token, jwt_required
from app.schemas.user_schema import user_schema, login_schema
from marshmallow import ValidationError
from datetime import timedelta

# Create a Blueprint for authentication routes
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input data
    try:
        user_schema.load(data)
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 400

    # Check if the username is already taken
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'The username is already taken. Please choose another.'}), 400

    # Check if the email is already registered
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'The email is already registered. Please use another or log in.'}), 400

    # Create a new user
    user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully', 'data': user_schema.dump(user)}), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input data
    try:
        login_schema.load(data, partial=('username',))
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 400

    # Check if the user exists
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Create an access token for the user
    access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(minutes=30))

    return jsonify({
        'message': 'User logged in successfully',
        'access_token': access_token,
        'data': user_schema.dump(user)
    }), 200


@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({'message': 'User logged out successfully'}), 200

