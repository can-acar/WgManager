class ListInterfaceCommand:
    def __init__(self, page: int = 1, per_page: int = 10, order_by: object = None, order: str = 'asc'):
        self.page = page
        self.per_page = per_page
        self.order_by = order_by
        self.order = order
