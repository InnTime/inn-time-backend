from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.blueprints.electives.models import ElectivesDistribution, Elective
from app.blueprints.users.models import User

electives = Blueprint('electives', __name__, )


@electives.route('/get_user_electives', methods=['GET'])
@jwt_required()
def get_user_electives():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    electives_id = ElectivesDistribution.query.filter_by(user_id=user.id).with_entities(
        ElectivesDistribution.elective_id).all()

    user_electives = [Elective.query.filter_by(id=elective_id[0]).first() for elective_id in electives_id]
    result = [{
        'name': elective.elective_name,
        'room': elective.classroom,
        'teacher': elective.teacher,
        'type': elective.type,
        'start_time': str(elective.start_time),
        'end_time': str(elective.end_time),
    } for elective in user_electives]
    return jsonify(result)


@electives.route('/get_electives', methods=['GET'])
def get_electives():
    all_electives = Elective.query.distinct(Elective.elective_name)
    result = [{
        'name': elective.elective_name,
        'type': elective.type,
    } for elective in all_electives]

    return jsonify(result)


@electives.route('/set_user_elective', methods=['POST'])
@jwt_required()
def set_user_elective():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    elective_name = request.json.get('elective_name')
    new_user_electives = Elective.query.filter_by(elective_name=elective_name).all()

    if new_user_electives is None:
        return jsonify({'error': 'Invalid elective name'}), 404

    existing_relation = ElectivesDistribution.query.filter_by(user_id=user.id,
                                                              elective_id=new_user_electives[0].id).first()
    if existing_relation:
        return jsonify({'error': 'User already has this elective'}), 400

    for elective in new_user_electives:
        new_relation = ElectivesDistribution(user_id=user.id, elective_id=elective.id)
        db.session.add(new_relation)
    db.session.commit()

    return jsonify({'message': 'Elective set successfully'}), 200


@electives.route('/delete_user_elective', methods=['DELETE'])
@jwt_required()
def delete_user_elective():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    elective_name = request.json.get('elective_name')
    electives_to_delete = Elective.query.filter_by(elective_name=elective_name).all()

    if electives:
        for elective in electives_to_delete:
            ElectivesDistribution.query.filter_by(elective_id=elective.id, user_id=user.id).delete()
        db.session.commit()
    else:
        return jsonify({'message': 'Elective not found'}), 400

    return jsonify({'message': 'Elective deleted successfully'}), 200
