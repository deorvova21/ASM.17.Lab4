import re
import urllib.request as rq
import urllib.parse as prs
from st20.truck import truck
from st20.car import car

class http_load:
    def __init__(self, url, nomer):
        self.url = url
        self.nomer = nomer
        res = rq.urlopen(self.url)
        html_data = str(res.read())
        self.student = re.search(r'student=(\d+)\">\[' + str(self.nomer) + '\]', html_data)\
            .group(1)

    def load_car(self, i):
        options = i.add_options()
        options['student'] = self.student
        req_url = self.url + '?' + prs.urlencode(options)
        rq.urlopen(req_url)
