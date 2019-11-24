import os

from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump
from app.rest import poem
from app.rest import hello
from app.config import get_env_config
from app.rest.healthcheck import dynamodb_available

def create_app():
    app = Flask(__name__)

    app.config.from_object(get_env_config(os.environ.get('FLASK_ENV', 'test')))

    app.register_blueprint(poem.blueprint)
    app.register_blueprint(hello.blueprint)

    # Healthcheck
    # TODO: can be isolated
    health = HealthCheck()
    health.add_check(dynamodb_available)
    app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())

    return app