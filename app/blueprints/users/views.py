from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import check_password_hash, generate_password_hash

from app import login_manager, db, jwt_manager
from app.blueprints.courses.models import Group
from app.blueprints.users.models import User

users = Blueprint('users', __name__, )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get_user_electives(int(user_id))


@users.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'accessToken': access_token}), 200

    return jsonify({'message': 'Invalid email or password'}), 401


@users.route('/register', methods=['POST'])
def register():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        jsonify({'message': 'Some information is missing'}), 400

    if User.query.filter_by(email=email).first():
        jsonify({'message': 'User with such an email exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 200


@users.route('/set_user_group', methods=['PUT'])
@jwt_required()
def set_user_group():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    data = request.json

    group_id = data.get('group_id')
    if not group_id:
        jsonify({'message': 'Group ID cannot be null'}), 400

    try:
        group_id = int(group_id)
    except ValueError:
        return jsonify({'message': 'Group ID is not an integer'}), 400

    if not Group.query.filter_by(id=group_id).first():
        jsonify({'message': 'There is no group with such an id'}), 400

    user.group_id = group_id
    db.session.commit()

    return jsonify({'message': 'Group set successfully'}), 200


@users.route('/get_user_group', methods=['GET'])
@jwt_required()
def get_user_group():
    user_id = get_jwt_identity()
    group_id = User.query.get(user_id).group_id

    return jsonify(group_id), 200


@users.route('/unset_user_group', methods=['PUT'])
@jwt_required()
def unset_user_group():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    user.group_id = None

    db.session.commit()

    return jsonify({'message': 'Group unset successfully'}), 200


@users.route('/update_user', methods=['PUT'])
@jwt_required()
def update_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    data = request.json

    password = data.get('password')
    if not password:
        jsonify({'message': 'Password cannot be null'}), 400

    user.password = generate_password_hash(password)

    db.session.commit()

    return jsonify({'message': 'User information updated successfully'}), 200


@users.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    jwt_manager.revoke_token(jti)

    return jsonify({'message': 'Logged out successfully'}), 200  # unset jwt cookies?
