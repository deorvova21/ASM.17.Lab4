import urllib

class food:

    def __init__(self):
        
        self.name = ""
        self.quantity = ""
        self.calories = ""


    def peredacha(self, idd):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd + "&name="+urllib.quote(self.name)+"&quantity="+urllib.quote(self.quantity)+"&calories="+urllib.quote(self.calories)+"&j=ok")
        
    
