import re
import urllib.request
import urllib.parse

from .Run import Run
from .Marathon import Marathon

SERVER_URL = "http://localhost:81/cgi-bin/lab3.py"


class Loader:
    def __init__(self, number):
        self.find(number)

    def find(self, number):
        with urllib.request.urlopen(SERVER_URL) as response:
           content = str(response.read())
           self.student = re.search(r'student=(\d+)\">\[' + str(number) + '\]', content).group(1)
        
    def makeUrl(self, run):
        params = {
            'student': self.student,
            'act': 'add',
            'length': run.length,
            'time': run.time,
            'date': run.date
        }
        
        if run.__class__.__name__ == 'Run':
            params['type'] = 'run'
        elif run.__class__.__name__ == 'Marathon':
            params['type'] = 'marathon'
            params['place'] = run.place
            
        return SERVER_URL + '?' + urllib.parse.urlencode(params)

    def load(self, run):
        try:
            urllib.request.urlopen(self.makeUrl(run))
            print("Загрузили запись от {0}.".format(run.date))
        except:
            print("Не удалось загрузить запись.")
        