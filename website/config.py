import os

HOSTNAME = '0.0.0.0'
PORT = 5000
DEBUG = True

BASEDIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'db/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db/db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True

SECRET_KEY = '9\xe9\xbfAf\xf2\x11\xf7u M\x7f\x9f\xae\xa6\x16\ta\xfb\rT\x84@\x96'
