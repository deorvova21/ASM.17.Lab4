import re
import urllib.request as rq
import urllib.parse as prs
from .Supervisor import Supervisor


class Util:
    def __init__(self, url, abs_id):
        self._url = url
        self._abs_id = abs_id
        self._id = self.get_student_id()
        print("Student id found: ", self._id)

    def get_student_id(self):
        response = rq.urlopen(self._url)
        print(self._url, " request successful")
        html_data = str(response.read())
        id = re.search(r'student=(\d+)\">\[' + str(self._abs_id) + '\]', html_data)\
            .group(1)
        return id

    def send_person(self, data):
        params = self._wrap_person(data)
        params['student'] = self._id
        print("Sending record with params: ", params)
        request_url = self._url + '?' + prs.urlencode(params)
        rq.urlopen(request_url)

    def _wrap_person(self, data):
        params = {'name': data._name, 'position': data._position,
                  'salary': data._salary, 'id': -1}
        if isinstance(data, Supervisor):
            params['action'] = 'save_supervisor'
            params['responsibility'] = data._responsibility
            params['liberties'] = data._liberties
        else:
            params['action'] = 'save_employee'
        return params
