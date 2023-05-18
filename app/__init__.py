# File: app/__init__.py
from flask import Flask

from app.controllers import InterfaceController


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    # from app.controllers import InterfaceController
    # from app.controllers import PeerController
    # from app.controllers import TunnelController
    # from app.controllers import UserController
    # from app.controllers import VpnController
    # from app.controllers import VpnServerController

    # call configure() on each controller
    InterfaceController.configure(app)


    return app
