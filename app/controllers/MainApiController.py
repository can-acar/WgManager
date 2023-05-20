from common.BaseController import BaseController


class MainApiController(BaseController):
    def __init__(self, mediator, app):
        super().__init__(app)
        self.mediator = mediator
