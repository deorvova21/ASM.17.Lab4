import urllib.request
import urllib.parse

class food:

    def __init__(self):
        
        self.name = ""
        self.quantity = ""
        self.calories = ""


    def peredacha(self, idd):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd + "&name="+urllib.parse.quote(self.name)+"&quantity="+urllib.parse.quote(self.quantity)+"&calories="+urllib.parse.quote(self.calories)+"&j=ok")
        
    
