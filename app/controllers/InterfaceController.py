from flask import request, Blueprint
from injector import inject
from mediatr import Mediator

from app.commands.AddInterfaceCommand import AddInterfaceCommand
from app.models.interface import Interface
from common import ApiResponse
# implementing BaseController
from common.BaseController import BaseController, not_found, error, ok, internal_server_error


class InterfaceApiController(BaseController):
    @inject
    def __init__(self, mediator: Mediator, app):
        super().__init__(app)
        self.mediator = mediator

    async def getAll(self) -> ApiResponse:
        try:
            data = request.get_json()
            interface = Interface(**data)
            command = AddInterfaceCommand(interface)
            result = await self.mediator.send_async(command)
            if result is None:
                return not_found(result)

            if not result.status:
                return error(result)

            return ok(result)

        except Exception as e:
            return internal_server_error(e)

    async def addInterface(self) -> ApiResponse:
        try:
            data = request.get_json()
            interface = Interface(**data)
            command = AddInterfaceCommand(interface)
            result = await self.mediator.send_async(command)
            if result is None:
                return not_found(result)

            if not result.status:
                return error(result)

            return ok(result)

        except Exception as e:
            return internal_server_error(e)


def configure(binder):
    binder.bind(InterfaceApiController, to=InterfaceApiController, scope=request)
    binder.bind(Mediator, to=Mediator, scope=request)


controller = InterfaceApiController
blueprint = Blueprint('Interface', __name__)
blueprint.add_url_rule('/api/interface.add', view_func=controller.addInterface, methods=['POST'])
blueprint.add_url_rule('/api/interface', view_func=controller.getAll, methods=['GET', 'POST'])

# blueprint.add_url_rule('', view_func=InterfaceApiController.as_view('addInterface'))
