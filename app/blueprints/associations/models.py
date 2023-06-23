from app import db


# TODO: add possibility to cancel weekly class


class groups_irregular_classes_table(db.Model):
    pass


groups_irregular_classes_table = db.Table(
    "groups_irregular_classes_table",
    db.Column("group_id", db.Integer, db.ForeignKey("group_table.id")),
    db.Column("irregular_class_id", db.Integer, db.ForeignKey("irregular_class_table.id")),
)

groups_weekly_classes_table = db.Table(
    "groups_weekly_classes_table",
    db.Column("group_id", db.Integer, db.ForeignKey("group_table.id")),
    db.Column("weekly_class_id", db.Integer, db.ForeignKey("weekly_class_table.id")),
)

courses_irregular_classes_table = db.Table(
    "courses_irregular_classes_table",
    db.Column("course_id", db.Integer, db.ForeignKey("course_table.id")),
    db.Column("irregular_class_id", db.Integer, db.ForeignKey("irregular_class_table.id")),
)

courses_weekly_classes_table = db.Table(
    "courses_weekly_classes_table",
    db.Column("group_id", db.Integer, db.ForeignKey("group_table.id")),
    db.Column("weekly_class_id", db.Integer, db.ForeignKey("weekly_class_table.id")),
)


class Group(db.Model):
    __tablename__ = 'group_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    year = db.Column(db.Integer)

    irregular_classes = db.relationship("IrregularClass", secondary=groups_irregular_classes_table)
    weekly_classes = db.relationship('WeeklyClass', secondary=groups_weekly_classes_table)
    users = db.relationship('User', back_populates='group')


class Course(db.Model):
    __tablename__ = 'course_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    is_elective = db.Column(db.Boolean, nullable=False, default=False)
    # TODO: add more fields here, like year, main professor, tg channel and so on

    irregular_classes = db.relationship('IrregularClass', secondary=courses_irregular_classes_table)
    weekly_classes = db.relationship('WeeklyClass', secondary=courses_weekly_classes_table)
