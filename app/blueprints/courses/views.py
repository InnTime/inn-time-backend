from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.blueprints.courses.models import Course, CoursesDistribution, Group

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
        'teacher': course.teacher,
        'start_time': course.start_time,
        'end_time': course.end_time,
        'day_of_week': course.day_of_week
    } for course in user_courses]

    return jsonify(result)


@courses.route('/get_courses', methods=['GET'])
def get_all_courses():
    all_courses = Course.query.all()
    result = [{
        'id': course.id,
        'name': course.course_name,
        'room': course.classroom,
        'teacher': course.teacher,
        'start_time': course.start_time,
        'end_time': course.end_time,
        'day_of_week': course.day_of_week
    } for course in all_courses]

    return jsonify(result)


@courses.route('/get_groups', methods=['GET'])
def get_all_groups():
    all_groups = Group.query.all()
    result = [{
        'id': group.id,
        'name': group.group_name,
        'type': group.type,
        'year': group.year,
        'number': group.number
    } for group in all_groups]

    return jsonify(result)
