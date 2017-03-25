from flask import Flask

import config as C

from views import blueprint as views_blueprint

app = Flask(__name__)


def setup_app(app):
    app.config.from_object('config')
    app.register_blueprint(views_blueprint)

def setup(app):
    setup_app(app)


def run(app):
    app.run(host=C.HOSTNAME, port=C.PORT, debug=C.DEBUG, threaded=True)
