from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig
from app.admin import AdminView

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message = 'Authorize to access'
login_manager.login_message_category = 'success'

jwt_manager = JWTManager()

admin = Admin()

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    config = DevelopmentConfig
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    jwt_manager.init_app(app)
    admin.init_app(app)

    from app.blueprints.courses.views import courses
    from app.blueprints.users.views import users
    from app.blueprints.electives.views import electives

    app.register_blueprint(courses)
    app.register_blueprint(electives)
    app.register_blueprint(users)

    from app.blueprints.users.models import User
    from app.blueprints.courses.models import Course, Group, CoursesDistribution
    from app.blueprints.electives.models import Elective, ElectivesDistribution
    from app.blueprints.courses.admin import CourseDistributionView
    from app.blueprints.electives.admin import ElectiveDistributionView
    from app.blueprints.users.admin import UserView

    admin.add_view(AdminView(Course, db.session))
    admin.add_view(AdminView(Elective, db.session))
    admin.add_view(UserView(User, db.session))
    admin.add_view(AdminView(Group, db.session))
    admin.add_view(CourseDistributionView(CoursesDistribution, db.session))
    admin.add_view(ElectiveDistributionView(ElectivesDistribution, db.session))

    return app
