from injector import inject
from app.models.interface import Interface
from app.repositories.InterfaceRepository import InterfaceRepository


class InterfaceService:
    @inject
    def __int__(self, repository: InterfaceRepository):
        self.repository = InterfaceRepository

    def addInterface(self, interface: Interface) -> Interface:
        self.repository.save(interface)

    def updateInterface(self, interface: Interface):
        self.repository.update(interface)

    def deleteInterface(self, id: int):
        interface = Interface(id=id)
        self.repository.delete(interface)

    def getInterface(self, id: int):
        return self.repository.get(id)

    def listInterface(self, offset, limit, search, sort, order):
        return self.repository.getListByFilter(limit, offset, search, sort, order)
