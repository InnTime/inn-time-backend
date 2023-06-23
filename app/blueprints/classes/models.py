from app import db
from sqlalchemy import Enum


class IrregularClass(db.Model):
    __tablename__ = 'irregular_class_table'

    id = db.Column(db.Integer, primary_key=True)
    classroom = db.Column(db.Integer)
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=False)


class WeeklyClass(db.Model):
    __tablename__ = 'weekly_class_table'

    id = db.Column(db.Integer, primary_key=True)
    classroom = db.Column(db.Integer)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    day_of_week = db.Column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
