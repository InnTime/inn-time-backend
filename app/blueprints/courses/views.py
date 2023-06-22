from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.blueprints.courses.models import Course

courses = Blueprint('courses', __name__, )


@courses.route('/get_courses', methods=['GET'])
@jwt_required()
def get():
    current_user = get_jwt_identity()
    user_group = current_user.group_id
    user_courses = Course.query.filter_by(group_id=user_group).all()
    result = [{
        'id': course.id,
        'name': course.course_name,
        'room': course.classroom,
        'start_time': course.start_time,
        'end_time': course.end_time,
    } for course in user_courses]

    return jsonify(result)
