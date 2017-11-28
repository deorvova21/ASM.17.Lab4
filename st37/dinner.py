from .drink import *
import pickle
import  re
import urllib

class dinner:
    
    f = "st37/kartoteka.pkl"
    kartoteka = []
    
    def __init__(self):
        pass

    def send(self):
        self.readfile()
        print(self.kartoteka)
        if (len(self.kartoteka)==0):
            print("Список пуст")
            return
        print("1")
        lab3 = str((urllib.urlopen("http://localhost:81/cgi-bin/lab3.py")).read())
        print("2")
        studnum = re.search(r'\d+', re.search(r'student=\d+\">\[37\]', lab3).group(0)).group(0)
        print("3")
        for i in self.kartoteka:
            print("!")
            i.peredacha(studnum)
            print("#")
            
    
    def readfile(self):
        s = open(dinner.f,"rb")
        self.kartoteka = pickle.load(s)
        print(self.kartoteka)

