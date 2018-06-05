from .Phone import *
import urllib.request
import urllib.parse

class Smartphone(Phone):

    def __init__(self):
        super().__init__()
        self.battery = ""
        self.camera_rez = ""

    def put(self, idd):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd + "&vendor="
                               + urllib.parse.quote(self.vendor)+"&model="+urllib.parse.quote(self.model)
                               + "&battery="+urllib.parse.quote(self.battery)
                               + "&camera=" + urllib.parse.quote(self.camera_res)+ "&act=sph")

