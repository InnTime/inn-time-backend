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

    from app.blueprints.courses.views import courses
    from app.blueprints.electives.views import electives
    from app.blueprints.users.views import users

    app.register_blueprint(courses)
    app.register_blueprint(electives)
    app.register_blueprint(users)

    from app.blueprints.courses.models import Course
    from app.blueprints.electives.models import Elective
    from app.blueprints.users.models import User

    admin.add_view(ModelView(Course, db.session))
    admin.add_view(ModelView(Elective, db.session))
    admin.add_view(ModelView(User, db.session))

    return app
