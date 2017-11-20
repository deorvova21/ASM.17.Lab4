import re
import urllib.request as rq
import urllib.parse as prs
from st17.VipDish import VipDish

class TransHTTP:
    def __init__(self, url, nomer):
        self.url = url
        self.nomer = nomer
        res = rq.urlopen(self.url)
        html_data = str(res.read())
        self.student = re.search(r'student=(\d+)\">\[' + str(self.nomer) + '\]', html_data)\
            .group(1)

    def SendDish(self, d):
        options = {'name': d.name,
                  'price': d.price,
                  'grams': d.grams,
                  'description': d.description,
                  'student':self.student,
                  'id': 0}
        
        if (isinstance(d, VipDish)):
            options['type'] = 1
            options['bonus'] = d.bonus
            options['calories'] = d.calories
        else:
            options['type'] = 0
            
        request_url = self.url + '?' + prs.urlencode(options)
        rq.urlopen(request_url)
