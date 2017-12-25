import re
import urllib.request as rq
import urllib.parse as prs
from st17.Dish import Dish
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
        options=d.GetOptions()
        options['student']=self.student
        request_url = self.url + '?' + prs.urlencode(options)
        rq.urlopen(request_url)
