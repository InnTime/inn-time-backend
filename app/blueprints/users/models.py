from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    group = db.relationship("Group", back_populates='users')

    electives = db.relationship('ElectivesDistribution', back_populates='user')

    def __str__(self):
        return self.email
