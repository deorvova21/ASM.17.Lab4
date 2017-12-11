import re
import urllib.request as rq
import urllib.parse as prs
from .Department import Department


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
        id = re.search(r'student=(\d+)\">\[' + self._abs_id + '\]', html_data)\
            .group(1)
        return id

    def send_market(self, data):
        params = self._wrap_market(data)
        params['student'] = self._id
        print("Sending record with params: ", params)
        request_url = self._url + '?' + prs.urlencode(params)
        rq.urlopen(request_url)

    def _wrap_market(self, data):
        params = {'nickname': data._nickname, 'owner_name': data._owner_name,
                  'address': data._address, 'id': -1}
        if isinstance(data, Department):
            params['action'] = 'save_department'
            params['product_type'] = data._product_type
            params['department_name'] = data._department_name
        else:
            params['action'] = 'save_market'
        return params
