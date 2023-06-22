import os
from datetime import timedelta

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET KEY'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'JWT SECRET KEY'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(weeks=2)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CSRF_ENABLED = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEVELOPMENT_DATABASE_URI') or 'postgresql://postgres:postgres@localhost:2101/inn-time'


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TESTING_DATABASE_URI') or 'postgresql://postgres:postgres@localhost:2101/inn-time'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'PRODUCTION_DATABASE_URI') or 'postgresql://postgres:postgres@localhost:2101/inn-time'
