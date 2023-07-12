import os
from datetime import timedelta

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'JWT_SECRET_KEY'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(weeks=2)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEVELOPMENT_DATABASE_URI') or 'postgresql://postgres:inn_time_db_password@db:5432/inn_time'


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TESTING_DATABASE_URI') or 'postgresql://postgres:inn_time_db_password@db:5432/inn_time'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'PRODUCTION_DATABASE_URI') or 'postgresql://postgres:inn_time_db_password@db:5432/inn_time'
