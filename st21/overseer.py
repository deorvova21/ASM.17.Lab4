from .prisoner import *


class Overseer(Prisoner):
    def __init__(self):
        super().__init__()
        self._salary = None
        self._phone_numb = None

    def send_data(self, url, stud_id):
        try:
            f = {'?student': stud_id, 'action': 'get_data', 'add': 'overseer', 'f_name': self._first_name,
                 'l_name': self._last_name, 'age': self._age, 'salary': self._salary, 'phone_numb': self._phone_numb}
            print (f)
            urllib.request.urlopen(url + urllib.parse.urlencode(f))
        except urllib.error.URLError:
            print('URLError')
        except Exception:
            print('some error in OVERSEER occurred')

