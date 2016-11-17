from __future__ import absolute_import

import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_ROOT, 'coast.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(APP_ROOT, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.getenv('COAST_SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'development_key'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'testing_key'


config = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "default": "config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('COAST_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)
