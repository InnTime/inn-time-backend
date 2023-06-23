from app import db


# TODO: add possibility to cancel weekly class


class GroupsIrregularClasses(db.Model):
    __tablename__ = 'groups_irregular_classes_table'

    group_id = db.Column(db.Integer, db.ForeignKey("group_table.id"), primary_key=True)
    group = db.relationship('Group', back_populates='groups_irregular_classes')

    irregular_class_id = db.Column(db.Integer, db.ForeignKey("irregular_class_table.id"), primary_key=True)
    irregular_class = db.relationship('IrregularClass', back_populates='groups_irregular_classes')


class GroupsWeeklyClasses(db.Model):
    __tablename__ = 'groups_weekly_classes_table'

    group_id = db.Column(db.Integer, db.ForeignKey("group_table.id"), primary_key=True)
    group = db.relationship('Group', back_populates='groups_weekly_classes')

    weekly_class_id = db.Column(db.Integer, db.ForeignKey("weekly_class_table.id"), primary_key=True)
    weekly_class = db.relationship('WeeklyClass', back_populates='groups_weekly_classes')


class CoursesIrregularClasses(db.Model):
    __tablename__ = 'courses_irregular_classes_table'

    course_id = db.Column(db.Integer, db.ForeignKey("course_table.id"), primary_key=True)
    course = db.relationship('Course', back_populates='courses_irregular_classes')

    irregular_class_id = db.Column(db.Integer, db.ForeignKey("irregular_class_table.id"), primary_key=True)
    irregular_class = db.relationship('IrregularClass', back_populates='courses_irregular_classes')


class CoursesWeeklyClasses(db.Model):
    __tablename__ = 'courses_weekly_classes_table'

    course_id = db.Column(db.Integer, db.ForeignKey("course_table.id"), primary_key=True)
    course = db.relationship('Course', back_populates='courses_weekly_classes')

    weekly_class_id = db.Column(db.Integer, db.ForeignKey("weekly_class_table.id"), primary_key=True)
    weekly_class = db.relationship('WeeklyClass', back_populates='courses_weekly_classes')


class Group(db.Model):
    __tablename__ = 'group_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    year = db.Column(db.Integer)

    users = db.relationship('User', back_populates='group')
    groups_irregular_classes = db.relationship('GroupsIrregularClasses', back_populates='group')
    groups_weekly_classes = db.relationship('GroupsWeeklyClasses', back_populates='group')


class Course(db.Model):
    __tablename__ = 'course_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    is_elective = db.Column(db.Boolean, nullable=False, default=False)
    # TODO: add more fields here, like year, main professor, tg channel and so on

    users_courses = db.relationship("UsersCourses", back_populates='course')
    courses_irregular_classes = db.relationship('CoursesIrregularClasses', back_populates='course')
    courses_weekly_classes = db.relationship('CoursesWeeklyClasses', back_populates='course')
