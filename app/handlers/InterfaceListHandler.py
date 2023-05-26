# class InterfaceListHandler:
#     # @inject
#     # def __init__(self, service: InterfaceService):
#     #     self.service = service
#
#     def handle(self, request: ListInterfaceCommand):
#         print("InterfaceListHandler")
#         return "InterfaceListHandler"

from app.commands import ListInterfaceCommand


# try:
#     result = await self.service.listInterface(request.page, request.per_page, request.order_by, request.order)
#     if result:
#         return result
#     else:
#         # throw exception
#         raise Exception("Interface not listed")
#
# except Exception as e:
#     raise Exception(str(e))


async def get_array_handler(request: ListInterfaceCommand):
    items = list()
    for i in range(0, request.items_count):
        items.append(i)
    return items
