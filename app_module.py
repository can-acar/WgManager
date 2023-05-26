from injector import Binder, inject, Module, singleton
from mediatr import Mediator

from app.db import AppDb
from app.handlers.InterfaceListHandler import get_array_handler
from common.BaseController import BaseController


class AppModule(Module):
    @inject
    def configure(self, binder: Binder):
        mediator = Mediator()

        # Mediator.register_handler(InterfaceListHandler)
        # Mediator.register_handler(InterfaceAddHandler)

        binder.bind(Mediator, to=mediator, scope=singleton)
        binder.bind(AppDb, to=AppDb, scope=singleton)
        binder.bind(BaseController, to=BaseController, scope=singleton)

        Mediator.register_handler(get_array_handler)

# binder.bind(InterfaceService, to=InterfaceService, scope=singleton)
# binder.bind(PeerService, to=PeerService, scope=singleton)
# binder.bind(InterfaceRepository, to=InterfaceRepository, scope=singleton)
# binder.bind(PeerRepository, to=PeerRepository, scope=singleton)

# binder.bind(InterfaceAddHandler, to=InterfaceAddHandler, scope=singleton)
# binder.bind(InterfaceListHandler, to=InterfaceListHandler, scope=singleton)
