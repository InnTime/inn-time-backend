from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import login_manager, db
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
        login_user(user)
        access_token = create_access_token(identity=str(user.id))
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid email or password'}), 401


@users.route('/register', methods=['POST'])
def register():
    data = request.json

    try:
        group_id = int(data.get('group_id'))
    except ValueError:
        return jsonify({'message': 'group_id is not an integer'}), 400

    if not Group.query.filter_by(id=group_id).first():
        jsonify({'message': 'There is no group with such an id'}), 400

    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        jsonify({'message': 'User with such an email exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password, group_id=group_id)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 200


@users.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json

    password = data.get('password')
    try:
        group_id = int(data.get('group_id'))
    except ValueError:
        return jsonify({'message': 'group_id is not an integer'}), 400

    if not Group.query.filter_by(id=group_id).first():
        jsonify({'message': 'There is no group with such an id'}), 400

    user.email = data.get('email')
    user.group_id = group_id
    user.password = generate_password_hash(password)

    db.session.commit()

    return jsonify({'message': 'User information updated successfully'}), 200


@users.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200  # fixme maybe we have to delete tokens after that
