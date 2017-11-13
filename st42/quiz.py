import re
import urllib.request as rq
import urllib.parse as prs
from .developed_rig import *


class Quiz:
    def __init__(self, url, abs_id):
        self._url = url
        self._abs_id = abs_id
        self._id = self.get_student_id()
        print("ID студента: ", self._id)

    def recieve_id_of_student(self):
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
        params = {'name': data._name, 'position': data._date,
                  'salary': data._capacity, 'id': -1}
        if isinstance(data, Developed_rif):
            params['action'] = 'save_developed_rig'
            params['source_nation'] = data._source_nation
            params['colour'] = data._colour
        else:
            params['action'] = 'save_drilling_rig'
        return params
