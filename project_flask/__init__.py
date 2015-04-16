from flask import Flask

from project_flask import config
from project_flask.first_app import first_app

from os import environ


def create_app(config=config.dev_config):
    mode = environ.get('MODE', 'dev')
    app = Flask("project_flask")
    app.config.from_object(
        'project_flask.config.{0}_config'.format(mode.lower()))

    register_blueprints(app)
    register_errorhandlers(app)
    register_jinja_env(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(first_app, url_prefix='/firstflask')


def register_errorhandlers(app):
    def render_error(e):
        if e.code == 400:
            return 'Bad request.', 400
        elif e.code == 404:
            return 'Not found.', 404
        elif e.code == 500:
            return 'Internal server error', 500

    for e in [400, 404, 500]:
        app.errorhandler(e)(render_error)


def register_jinja_env(app):
    pass


def register_extensions(app):
    pass
