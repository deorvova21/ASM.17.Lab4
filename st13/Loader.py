import urllib.parse
import urllib.request
import re

from .Person import Person


class Loader:
    def __init__(self, student_id):
        self.student = ''
        self.url = "http://localhost:81/cgi-bin/lab3.py"
        self.find_id(student_id)

    def find_id(self, student_id):
        res = urllib.request.urlopen(self.url)
        lab3 = str(res.read())
        res.close()
        num = re.search(r'student=(\d+)\">\[' + student_id + '\]', lab3).group(1)
        self.student = '&student={0}'.format(num)

    def _request(self, params):
        url = self.url + '?' + params + self.student
        urllib.request.urlopen(url)


    @staticmethod
    def create_person_params(model):
        return {'first_name': model.first_name, 'last_name': model.last_name, 'age': model.age}

    @staticmethod
    def create_director_params(model):
        params = {'salary': model.salary, 'degree': model.degree, 'workplace': model.workplace}
        return {**Loader.create_person_params(model), **params}

    def send(self, model):
        print(model)
        try:
            if type(model) is Person:
                params = {**Loader.create_person_params(model), **{'act': '0'}}
            else:
                params = {**Loader.create_director_params(model), **{'act': '1'}}
            self._request(Loader.bind_params(params))
        except:
            print('error')

    @staticmethod
    def bind_params(params):
        str = ''
        for key, value in params.items():
            str += '&{0}={1}'.format(key, urllib.parse.quote(value))
        return str
