import asyncio

from flask import Blueprint, request
from injector import inject
from mediatr import Mediator

from app.commands.AddInterfaceCommand import AddInterfaceCommand
from app.commands.ListInterfaceCommand import ListInterfaceCommand
from common import ApiResponse
from common.BaseController import BaseController, not_found, error, ok, internal_server_error

bp = Blueprint('Interface', __name__)


class ListAllApiController(BaseController):

    @inject
    def __init__(self, mediator: Mediator) -> object:
        super().__init__()
        self.mediator = mediator

        # self.bp =

    async def get(self) -> ApiResponse:
        try:
            # data = request.get_json()
            # command = ListInterfaceCommand(**data)
            # result = await self.mediator.send_async(command)
            #
            # if result is None:
            #     return not_found(result)
            #
            # if not result.status:
            #     return error(result)

            return ok(['sdf','asdasd'])
        except Exception as e:
            return internal_server_error(e, 'Error')


class AddInterfaceApiController(BaseController):

    @inject
    def __init__(self, mediator: Mediator) -> object:
        super().__init__()
        self.mediator = mediator

        # self.bp =

    async def post(self):
        try:
            data = request.get_json()
            command = AddInterfaceCommand(**data)
            result = await self.mediator.send_async(command)

            if result is None:
                return not_found(result)

            if not result.status:
                return error(result)

            return ok(result)

        except Exception as e:
            return internal_server_error(e)


bp.add_url_rule('/api/interface.list', view_func=ListAllApiController.as_view('list_api'), methods=['GET', 'POST'])
bp.add_url_rule('/api/interface.add', view_func=AddInterfaceApiController.as_view('add_api'), methods=['POST'])
