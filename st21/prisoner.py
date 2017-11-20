class Prisoner:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._age = None

    def output_data(self, data):
        data.clear()
        data.append(self._first_name)
        data.append(self._last_name)
        data.append(self._age)
