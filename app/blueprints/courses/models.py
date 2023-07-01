from sqlalchemy import Enum

from app import db


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(10), unique=True, nullable=False)
    type = db.Column(Enum('B', 'M', name='group_type_enum'))
    year = db.Column(db.Integer)
    number = db.Column(db.Integer)

    users = db.relationship('User', back_populates='group')
    courses = db.relationship('CoursesDistribution', back_populates='group')

    def __str__(self):
        return self.group_name


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), unique=True, nullable=False)
    classroom = db.Column(db.Integer)
    teacher = db.Column(db.String(50))
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    day_of_week = db.Column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                                 'Friday', 'Saturday', 'Sunday', name='days_of_week_enum'))

    groups = db.relationship('CoursesDistribution', back_populates='course')

    def __str__(self):
        return self.course_name


class CoursesDistribution(db.Model):
    __tablename__ = 'courses_distribution'

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id', ondelete='CASCADE'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id', ondelete='CASCADE'), primary_key=True)

    course = db.relationship('Course', back_populates='groups')
    group = db.relationship('Group', back_populates='courses')
