from app.models.interface import Interface


# message is string


class AddInterfaceResult:
    # status: bool
    # message: str
    # data: any
    def __init__(self, status: bool, message: str, data: any = None):
        self.status = status
        self.message = message
        self.data = data


class AddInterfaceCommand:
    def __init__(self, interface: Interface) -> AddInterfaceResult:
        self.interface = interface

    # return cast to ApiResponse
    # @property
    # def to_json(self):
    #     return ApiResponse

    # return cast to ApiResponse
    # @property
    # def to_json(self):
    #     return ApiResponse
