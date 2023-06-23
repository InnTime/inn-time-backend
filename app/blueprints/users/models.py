from flask_login import UserMixin

from app import db


class UsersCourses(db.Model):
    __tablename__ = 'users_courses_table'

    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"), primary_key=True)
    user = db.relationship('User', back_populates='users_courses')

    course_id = db.Column(db.Integer, db.ForeignKey("course_table.id"), primary_key=True)
    course = db.relationship('Course', back_populates='users_courses')


class User(UserMixin, db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey("group_table.id"))
    group = db.relationship("Group", back_populates='users')
    users_courses = db.relationship("UsersCourses", back_populates='user')
