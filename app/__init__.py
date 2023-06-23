from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message = 'Authorize to access'
login_manager.login_message_category = 'success'

jwt_manager = JWTManager()

admin = Admin()

migrate = Migrate()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    jwt_manager.init_app(app)
    admin.init_app(app)

    '''
    from app.blueprints.courses.views import courses
    from app.blueprints.electives.views import electives
    from app.blueprints.users.views import users

    app.register_blueprint(courses)
    app.register_blueprint(electives)
    app.register_blueprint(users)
    '''

    from app.blueprints.associations.models import groups_irregular_classes_table, groups_weekly_classes_table, \
        courses_irregular_classes_table, courses_weekly_classes_table, Group, Course
    from app.blueprints.classes.models import IrregularClass, WeeklyClass
    from app.blueprints.users.models import users_courses_table, User

    # admin.add_view(ModelView(groups_irregular_classes_table, db.session))
    # admin.add_view(ModelView(groups_weekly_classes_table, db.session))
    # admin.add_view(ModelView(courses_irregular_classes_table, db.session))
    # admin.add_view(ModelView(courses_weekly_classes_table, db.session))
    # admin.add_view(ModelView(Group, db.session))
    # admin.add_view(ModelView(Course, db.session))
    # admin.add_view(ModelView(IrregularClass, db.session))
    # admin.add_view(ModelView(WeeklyClass, db.session))
    # admin.add_view(ModelView(users_courses_table, db.session))
    # admin.add_view(ModelView(User, db.session))

    return app
