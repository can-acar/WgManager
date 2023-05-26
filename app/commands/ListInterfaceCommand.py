class ListInterfaceResult:
    status: str
    message: str
    data: any

    def __init__(self, status: str = None, message: str = None, data: any = None):
        self.status = status
        self.message = message
        self.data = data


class ListInterfaceCommand:
    page: int = 1
    per_page: int = 10
    order_by: list = [{'order': 'Id', 'by': 'asc'}, {'order': 'Name', 'by': 'asc'}]
    query: str

    def __init__(self, page: int = 1, per_page: int = 10, order_by: list = None, query: str = None):
        if order_by is None:
            order_by = []

        self.page = page
        self.per_page = per_page
        self.order_by = order_by
        self.query = query
