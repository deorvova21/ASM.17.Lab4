import urllib.request
import urllib.parse

class Drilling_rig:

    def __init__(self):
 
        self.name = ""
        self.date = ""
        self.capacity = ""


    def send(self):
         urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd + "&name="+urllib.parse.quote(self.name)+"&date="+urllib.parse.quote(self.date)+"&capacity="+urllib.parse.quote(self.capacity)+"&j=ok")
    
