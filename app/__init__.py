from flask import Flask
from flask_admin import Admin
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.admin import AdminView
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt_manager = JWTManager()
cors = CORS(supports_credentials=True)


def create_app():
    admin = Admin()

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    initialize_extensions(app, admin)
    register_blueprints(app)
    register_admin_views(admin)

    return app


def initialize_extensions(app, admin):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    jwt_manager.init_app(app)
    admin.init_app(app)
    cors.init_app(app)


def register_blueprints(app):
    from app.blueprints.courses.views import courses
    from app.blueprints.users.views import users
    from app.blueprints.electives.views import electives

    app.register_blueprint(courses)
    app.register_blueprint(electives)
    app.register_blueprint(users)


def register_admin_views(admin):
    from app.blueprints.users.models import User
    from app.blueprints.courses.models import Course, Group, CoursesDistribution
    from app.blueprints.electives.models import Elective, ElectivesDistribution
    from app.blueprints.courses.admin import CourseDistributionView, GroupView
    from app.blueprints.electives.admin import ElectiveDistributionView
    from app.blueprints.users.admin import UserView

    admin.add_view(AdminView(Course, db.session))
    admin.add_view(AdminView(Elective, db.session))
    admin.add_view(UserView(User, db.session))
    admin.add_view(GroupView(Group, db.session))
    admin.add_view(CourseDistributionView(CoursesDistribution, db.session))
    admin.add_view(ElectiveDistributionView(ElectivesDistribution, db.session))
