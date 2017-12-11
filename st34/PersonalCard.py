class PersonalCard:
    _first_name: str = ''
    _last_name: str = ''
    _birth_date: str = ''

    def get_parameters(self):
        return {'is_parent': 'True', 'first_name': self._first_name, 'last_name': self._last_name,
                'birth_date': self._birth_date}
