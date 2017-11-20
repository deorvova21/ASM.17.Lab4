import re
import urllib.request as rq
import urllib.parse as prs
from st20.truck import truck

class http_load:
    def __init__(self, url, nomer):
        self.url = url
        self.nomer = nomer
        res = rq.urlopen(self.url)
        html_data = str(res.read())
        self.student = re.search(r'student=(\d+)\">\[' + str(self.nomer) + '\]', html_data)\
            .group(1)

    def load_car(self, c):
        options = {'gosnomer': c.gosnomer,
                   'mark': c.mark,
                   'model': c.model,
                   'horsepower': c.horsepower,
                   'mileage':c.mileage,
                   'student':self.student,
                   'id': 0}
        
        if (isinstance(c, truck)):
            options['type'] = 'add_truck'
            options['height'] = c.height
            options['carrying'] = c.carrying
        else:
            options['type'] = 'add_car'
            
        req_url = self.url + '?' + prs.urlencode(options)
        rq.urlopen(req_url)
