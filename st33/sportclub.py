from .Champion import *
import pickle
import urllib.request
import urllib.parse
import re

class Sportclub:
    
    def __init__(self):
        self.sportclub = []
        
    def load(self):
        self.sportclub = pickle.load(open("st33/dump.pkl", "rb"))
        
    def send(self):
        my_num = re.search(r'<a href=\"\/cgi-bin\/lab3\.py\?student=(\d+)\">\[33\]', 
            str(urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py").read())
            ).group(1)

        if self.sportclub: 
            for e in self.sportclub:
                if type(e) is Sportsman:
                    #'http://localhost:81/cgi-bin/lab3.py?student=20&id=-1&action=save_sportsman&full_name=1&age=1&rating=1'
                    #'http://localhost:81/cgi-bin/lab3.py?student=20&action=save_sportsman&full_name=1&age=1&rating=11'
                    str1 = "http://localhost:81/cgi-bin/lab3.py?student=" + str(my_num) + "&id=-1&action=save_sportsman&full_name=" + urllib.parse.quote(str(e.getFull_name()))\
                                           + "&age=" + urllib.parse.quote(str(e.getAge())) + "&rating=" + urllib.parse.quote(str(e.getRating()))
                    urllib.request.urlopen(str1)
                    #print(str1)
                if type(e) is Champion:
                    urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?student=" + str(my_num) + "&id=-1&action=save_sportsman&full_name="
                                           + urllib.parse.quote(str(e.getFull_name())) + "&age=" + urllib.parse.quote(str(e.getAge())) + "&rating="
                                           + urllib.parse.quote(str(e.getRating())) + "&wins=" + urllib.parse.quote(str(e.getWins())))
        else:
            print("Нет")
