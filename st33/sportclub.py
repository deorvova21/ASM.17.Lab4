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
                dat = e.read()
                str1 = "http://localhost:81/cgi-bin/lab3.py?student=" + str(my_num) + "&id=-1&action=save_sportsman"+dat
                urllib.request.urlopen(str1)
                    

        else:
            print("Нет")
