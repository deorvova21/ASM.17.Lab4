from .Employee import Employee

class Supervisor(Employee):
    def __init__(self):
        super().__init__()
        self._responsibility = None
        self._liberties = None