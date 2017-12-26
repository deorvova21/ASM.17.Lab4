from .drilling_rig import *


class Developed_rig(Drilling_rig):
    
    def __init__(self):
        super().__init__()
        self.source_nation = ""
        self.colour = ""


    def send(self):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd +"&name="+urllib.parse.quote(self.name)+"&date="+urllib.parse.quote(self.date)+"&capacity="+urllib.parse.quote(self.capacity)+"&source_nation="+urllib.parse.quote(self.source_nation)+"&colour="+urllib.parse.quote(self.colour)+"&j=okok")
