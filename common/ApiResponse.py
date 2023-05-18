from flask import jsonify


class ApiResponse:
    def __init__(self, status: bool, message: str, data: any = None):
        self.status = status
        self.message = message
        self.data = data

    # return
    # {
    #     "status": "success",
    #     "message": "Interface added successfully",
    #     "data": {
    #         "name": "wg0",
    #         "description": "Wireguard interface",
    #         "gateway": "
    #         "ipv4": "
    #         "ipv6": "
    #         "listen_port": "
    #         "on_up": "
    #         "on_down": "
    #         "private_key": "
    #         "public_key": "
    #     }
    # }
    # def to_json(self):
    #     return {
    #         "status": self.status,
    #         "message": self.message,
    #         "data": self.data
    #     }

    # I want to access this method like this in  async def addInterface(self) -> ApiResponse:
    # ok(result)
    # error(result)
    # not_found(result)
    # internal_server_error(result)
    # where result is ApiResponse
    # return cast to ApiResponse
    # @property

    @property
    def ok(self, data: any = None, message: str = None):
        self.status = True
        self.message = message
        self.data = data
        return jsonify(self), 200

    @property
    def error(self, data: any = None, message: str = None):
        self.status = False
        self.message = message
        self.data = data
        return jsonify(self), 400

    @property
    def not_found(self, data: any = None, message: str = None):
        self.status = False
        self.message = message
        self.data = data
        return jsonify(self), 404

    @property
    def internal_server_error(self, data: any = None, message: str = None):
        self.status = False
        self.message = message
        self.data = data
        return jsonify(self), 500
