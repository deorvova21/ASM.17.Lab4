import re
import urllib.request as rq
import urllib.parse as prs
from st32.Employee import Employee

class Transport:
    def __init__(self, url, nomer):
        self.url = url
        self.nomer = nomer
        res = rq.urlopen(self.url)
        html_data = str(res.read())
        self.student = re.search(r'student=(\d+)\">\[' + str(self.nomer) + '\]', html_data)\
            .group(1)

    def Send(self, obj):
        options = {'OrganizationName': obj.OrganizationName,
                  'DepName': obj.DepName,
                  'Floor': obj.Floor,
                  'info': obj.info,
                  'student':self.student}
        
        if (isinstance(obj, Employee)):
            options['type'] = 2
            options['FullName'] = obj.FullName
            options['Age'] = obj.Age
            options['PhoneNum'] = obj.PhoneNum
            options['Salary'] = obj.Salary
        else:
            options['type'] = 1
            
        request_url = self.url + '?' + prs.urlencode(options)
        rq.urlopen(request_url)
