from .vipclient import *
import pickle
import urllib.request
import urllib.parse
import re
class Customers:
    def __init__(self):
        self.customer = []
    def load(self):
        self.customer = pickle.load( open( "st01/pickledata.p", "rb" ) )
    def send(self):
        my_num = re.search(r'<a href=\"\/cgi-bin\/lab3\.py\?student=(\d+)\">\[01\]', 
            str(urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py").read())
            ).group(1)

        if self.customer: 
            for e in self.customer:
                if type(e) is Client:
                    urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?student=" + str(my_num) + "&action=1&name=" + urllib.parse.quote(str(e.getName())) + "&age=" + urllib.parse.quote(str(e.getAge())) + "&weight=" + urllib.parse.quote(str(e.getWeight())) + "&phone=" + urllib.parse.quote(str(e.getPhone())) + "&typeadd=1")                
                if type(e) is Vipclient:
                    urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?student=" + str(my_num) + "&action=1&name=" + urllib.parse.quote(str(e.getName())) + "&age=" + urllib.parse.quote(str(e.getAge())) + "&weight=" + urllib.parse.quote(str(e.getWeight())) + "&phone=" + urllib.parse.quote(str(e.getPhone()))+ "&parking_place=" + urllib.parse.quote(str(e.getParkingPlace()))+ "&personal_trener=" + urllib.parse.quote(str(e.getPersonalTrener())) + "&typeadd=2")
        else:
            print("Не ")