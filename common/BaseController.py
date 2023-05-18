from common.ApiResponse import ApiResponse


def ok(data: any = None, message: str = None):
    return ApiResponse(status=True, message=message, data=data).ok()


def error(data: any = None, message: str = None):
    return ApiResponse(status=False, message=message, data=data).error()


def not_found(data: any = None, message: str = None):
    return ApiResponse(status=False, message=message, data=data).not_found()


def internal_server_error(data: any = None, message: str = None):
    return ApiResponse(status=False, message=message, data=data).internal_server_error()


class BaseController:
    def __init__(self, app):
        self.app = app
