from .Market import Market

class Department(Market):
    def __init__(self):
        super().__init__()
        self._product_type = None
        self._department_name = None