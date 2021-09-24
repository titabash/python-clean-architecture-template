from flask import Flask

# from flask_settings import DevConfig
from controller import hello_controller


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_object)
    app.register_blueprint(hello_controller.blueprint)
    return app
