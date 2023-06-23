from app import db


class Elective(db.Model):
    __tablename__ = 'electives'

    id = db.Column(db.Integer, primary_key=True)
    elective_name = db.Column(db.String(50), unique=True, nullable=False)
    classroom = db.Column(db.Integer)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    users = db.relationship('ElectivesDistribution', back_populates='elective')


class ElectivesDistribution(db.Model):
    __tablename__ = 'electives_distribution'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    elective_id = db.Column(db.Integer, db.ForeignKey('electives.id', ondelete='CASCADE'), primary_key=True)

    user = db.relationship('User', back_populates='electives')
    elective = db.relationship('Elective', back_populates='users')

