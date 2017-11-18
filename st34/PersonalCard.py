class PersonalCard:
    _first_name: str = ''
    _last_name: str = ''
    _birth_date: str = ''

    def __init__(self, a, b, c):
        self._first_name = a
        self._last_name = b
        self._birth_date = c
        pass

    def get_parameters(self):
        return {'is_parent': 'True', 'first_name': self._first_name, 'last_name': self._last_name,
                'birth_date': self._birth_date}
