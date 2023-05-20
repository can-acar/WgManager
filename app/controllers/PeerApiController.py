from injector import inject
from mediatr import Mediator

from common.BaseController import BaseController


class PeerApiController(BaseController):
    @inject
    def __init__(self, mediator: Mediator, app):
        super().__init__(app)
        self.mediator = mediator
