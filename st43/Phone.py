import urllib.request
import urllib.parse

class Phone:
    def __init__(self):
        self.vendor = ""
        self.model = ""

    def put(self, idd):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd + "&vendor="
                               + urllib.parse.quote(self.vendor)+"&model="+urllib.parse.quote(self.model)+"&act=ph")

