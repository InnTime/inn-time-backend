from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.blueprints.electives.models import Distribution, Elective

electives = Blueprint('electives', __name__, )


@electives.route('/get_electives', methods=['GET'])
@jwt_required()
def get():
    current_user = get_jwt_identity()
    electives_id = Distribution.query.filter_by(user_id=current_user.id).all()
    user_electives = [Elective.query.filter_by(id=elective_id).first() for elective_id in electives_id]
    result = [{
        'id': elective.id,
        'name': elective.course_name,
        'room': elective.classroom,
        'start_time': elective.start_time,
        'end_time': elective.end_time,
    } for elective in user_electives]

    return jsonify(result)
