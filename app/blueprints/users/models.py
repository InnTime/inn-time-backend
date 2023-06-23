from flask_login import UserMixin

from app import db


users_courses_table = db.Table(
    "users_courses_table",
    db.Column("user_id", db.Integer, db.ForeignKey("user_table.id")),
    db.Column("course_id", db.Integer, db.ForeignKey("course_table.id")),
)


class User(UserMixin, db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey("group_table.id"))
    group = db.relationship("Group", back_populates='users')
    courses = db.relationship('Course', secondary=users_courses_table)
