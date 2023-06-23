from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.blueprints.electives.models import ElectivesDistribution, Elective

electives = Blueprint('electives', __name__, )


@electives.route('/get_user_electives', methods=['GET'])
@jwt_required()
def get_user_electives():
    current_user = get_jwt_identity()
    electives_id = ElectivesDistribution.query.filter_by(user_id=current_user.id).with_entities(
        ElectivesDistribution.elective_id).all()

    user_electives = [Elective.query.filter_by(id=elective_id[0]).first() for elective_id in electives_id]
    result = [{
        'id': elective.id,
        'name': elective.course_name,
        'room': elective.classroom,
        'start_time': elective.start_time,
        'end_time': elective.end_time,
    } for elective in user_electives]

    return jsonify(result)


@electives.route('/get_electives', methods=['GET'])
def get_user_electives():
    all_electives = Elective.query.all()
    result = [{
        'id': elective.id,
        'name': elective.course_name,
        'room': elective.classroom,
        'start_time': elective.start_time,
        'end_time': elective.end_time,
    } for elective in all_electives]

    return jsonify(result)


@electives.route('/set_elective', methods=['POST'])
@jwt_required()
def set_elective():
    current_user = get_jwt_identity()

    elective_id = request.json.get('elective_id')
    elective = Elective.query.filter_by(id=elective_id).first()

    if elective is None:
        return jsonify({'error': 'Invalid elective ID'}), 404

    existing_relation = ElectivesDistribution.query.filter_by(user_id=current_user.id, elective_id=elective_id).first()
    if existing_relation:
        return jsonify({'error': 'User already has this elective'}), 400

    new_relation = ElectivesDistribution(user_id=current_user.id, elective_id=elective_id)
    db.session.add(new_relation)
    db.session.commit()

    return jsonify({'message': 'Elective set successfully'})
