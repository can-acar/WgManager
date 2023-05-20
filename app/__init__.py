from flasgger import Swagger
from flask import Flask, Blueprint
from flask_injector import FlaskInjector
from app.controllers.InterfaceApiController import bp as interface_api

from app_module import AppModule


def create_app():
    app = Flask(__name__)

    bp = Blueprint('app', __name__)

    app.config['DATABASE_URI'] = 'sqlite:///wireguard.db'

    app.register_blueprint(interface_api)

    Swagger(app)

    app.config.from_object('config')

    before_first_request_funcs = []
    app.before_first_request_funcs = before_first_request_funcs

    FlaskInjector(app=app, modules=[AppModule])

    app.debug = True

    return app
