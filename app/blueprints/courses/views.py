from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.blueprints.courses.models import Course, CoursesDistribution

courses = Blueprint('courses', __name__, )


@courses.route('/get_user_courses', methods=['GET'])
@jwt_required()
def get_user_courses():
    current_user = get_jwt_identity()
    courses_id = CoursesDistribution.query.filter_by(group_id=current_user.group_id).with_entities(
        CoursesDistribution.course_id).all()

    user_courses = [Course.query.filter_by(id=course_id[0]).first() for course_id in courses_id]
    result = [{
        'id': course.id,
        'name': course.course_name,
        'room': course.classroom,
        'start_time': course.start_time,
        'end_time': course.end_time,
    } for course in user_courses]

    return jsonify(result)


@courses.route('/get_courses', methods=['GET'])
def get_user_electives():
    all_courses = Course.query.all()
    result = [{
        'id': course.id,
        'name': course.course_name,
        'room': course.classroom,
        'start_time': course.start_time,
        'end_time': course.end_time,
    } for course in all_courses]

    return jsonify(result)
