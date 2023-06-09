from flask import Flask
from injector import inject
from mediatr import Mediator

from app.commands import AddInterfaceCommand
from app.commands.AddInterfaceCommand import AddInterfaceResult
from app.services import InterfaceService

app = Flask(__name__)


@Mediator.handler
class InterfaceAddHandler:
    mediatr: Mediator

    @inject
    def __init__(self, service: InterfaceService):
        self.service = service

    async def handle_async(self, command: AddInterfaceCommand) -> AddInterfaceResult:
        try:
            result = await self.service.addInterface(**command.interface)
            if result:
                return AddInterfaceResult(status="success", message="Interface added successfully", data=result)
            else:
                # throw exception
                raise Exception("Interface not added")

        except Exception as e:
            return AddInterfaceResult(status="error", message=str(e), data=None)

    def get(self):
        self.write("InterfaceAddHandler")
    # Path: app\handlers\InterfaceDeleteHandler.py

    # Compare this snippet from app\services\InterfaceService.py:
