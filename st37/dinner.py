from .drink import *
import pickle
import  re
import urllib.request

class dinner:
    
    f = "st37/kartoteka.pkl"
    kartoteka = []
    
    def __init__(self):
        pass

    def send(self):
        if (len(self.kartoteka)==0):
            print("Список пуст")
            return
        lab3 = str(urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py").read())
        studnum = re.search(r'\d+', re.search(r'student=\d+\">\[37\]', lab3).group(0)).group(0)
        for i in self.kartoteka:
            i.peredacha(studnum)
            print(i)
            
    
    def readfile(self):
        s = open(dinner.f,"rb")
        self.kartoteka = pickle.load(s)
        return self.kartoteka
