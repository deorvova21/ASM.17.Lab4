from .food import *


class drink(food):
    
    def __init__(self):
        super().__init__()
        self.alcogol = ""
       


    def peredacha(self, idd):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd +"&name="+urllib.parse.quote(self.name)+"&quantity="+urllib.parse.quote(self.quantity)+"&calories="+urllib.parse.quote(self.calories)+"&alcogol="+urllib.parse.quote(self.alcogol)+"&j=okok")
        
