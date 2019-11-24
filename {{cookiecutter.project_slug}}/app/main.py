import os

from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump
from app.rest import hello
from app.config import get_env_config

def create_app():
    app = Flask(__name__)

    app.config.from_object(get_env_config(os.environ.get('FLASK_ENV', 'test')))

    app.register_blueprint(hello.blueprint)

    # Healthcheck
    # TODO: can be isolated
    health = HealthCheck()
    app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())

    return app

