from .food import *


class drink(food):
    
    def __init__(self):
        super().__init__()
        self.alcogol = ""
       


    def peredacha(self, idd):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd +"&name="+urq.quote(self.name)+"&quantity="+urq.quote(self.quantity)+"&calories="+urq.quote(self.calories)+"&alcogol="+urq.quote(self.alcogol))
        
