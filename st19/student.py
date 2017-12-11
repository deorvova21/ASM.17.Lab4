import urllib.request
import urllib.parse

class Student:
    def __init__(self):
        self.name = ""
        self.sex = ""
        self.age = ""
        self.grants = ""     

    def peredacha(self, idd):
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + idd + "&name="+urllib.parse.quote(self.name)+"&sex="+urllib.parse.quote(self.sex)+"&age="+urllib.parse.quote(self.age)+"&grants="+urllib.parse.quote(self.grants)+"&i=ok")


