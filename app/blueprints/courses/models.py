from sqlalchemy import Enum

from app import db


class Group(db.Model):

    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(10), unique=True, nullable=False)
    group_year = db.Column(db.Integer)

    courses = db.relationship('CourseGroup', back_populates='course')


class Course(db.Model):

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), nullable=False)
    classroom = db.Column(db.Integer)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    day_of_week = db.Column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    group = db.relationship('Group', back_populates='courses')
