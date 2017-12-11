from .student import *

class mayor(Student):
    def __init__(self):
        super().__init__()
        self.telephone = ""
        self.doljnost = ""

    def peredacha(self, idd):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd +"&name="+urllib.parse.quote(self.name)+"&sex="+urllib.parse.quote(self.sex)+"&age="+urllib.parse.quote(self.age)+"&grants="+urllib.parse.quote(self.grants)+"&telephone="+urllib.parse.quote(self.telephone)+"&doljnost="+urllib.parse.quote(self.doljnost)+"&i=okok")        
        

    


