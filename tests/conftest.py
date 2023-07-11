import pytest
from app import create_app, db
from app.blueprints.users.models import User
from app.blueprints.courses.models import Course, Group, CoursesDistribution
from app.blueprints.electives.models import Elective, ElectivesDistribution


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    with app.app_context():
        # clean up / reset resources here
        db.session.query(User).delete()
        db.session.query(Course).delete()
        db.session.query(Group).delete()
        db.session.query(Elective).delete()
        db.session.query(CoursesDistribution).delete()
        db.session.query(ElectivesDistribution).delete()
        db.session.commit()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
