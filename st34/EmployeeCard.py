from .PersonalCard import *


class EmployeeCard(PersonalCard):
    _job_title: int = 0

    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self._job_title = d

    def get_parameters(self):
        return {'is_parent': 'False', 'first_name': self._first_name, 'last_name': self._last_name,
                'birth_date': self._birth_date, 'job_title': self._job_title}
