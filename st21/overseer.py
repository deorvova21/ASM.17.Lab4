from .prisoner import *


class Overseer(Prisoner):
    def __init__(self):
        super().__init__()
        self._salary = None
        self._phone_numb = None

    def output_data(self, data):
        super().output_data(data)
        data.append(self._salary)
        data.append(self._phone_numb)
