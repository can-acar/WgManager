from injector import inject
from mediatr import Mediator

from app.commands import ListInterfaceCommand
from app.services import InterfaceService


@inject
@Mediator.handler(ListInterfaceCommand)
class InterfaceListHandler:
    def __init__(self, service: InterfaceService):
        self.service = service

    async def handle_async(self, command: ListInterfaceCommand):
        try:
            result = await self.service.listInterface(command.page, command.per_page, command.order_by, command.order)
            if result:
                return result
            else:
                # throw exception
                raise Exception("Interface not listed")

        except Exception as e:
            raise Exception(str(e))

    def get(self):
        self.write("InterfaceListHandler")
