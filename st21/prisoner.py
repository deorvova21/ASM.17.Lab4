import urllib.parse
import urllib.request


class Prisoner:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._age = None

    def send_data(self, url, stud_id):
        try:
            f = {'?student': stud_id, 'action': 'get_data', 'add': 'prisoner', 'f_name': self._first_name,
                 'l_name': self._last_name, 'age': self._age}
            print(f)
            urllib.request.urlopen(url + urllib.parse.urlencode(f))
        except urllib.error.URLError:
            print('URLError')
        except Exception:
            print('some error PRISONER occurred')
