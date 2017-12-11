from .mayor import *
import pickle
import re
import urllib.request

class group:    
    spisok = []
    Gubkin = 'st19/file.pkl'

    def __init__(self):
        pass

    def send(self):
        if (len(self.spisok)==0):
            print("Список пуст")
            return
        lab3 = str(urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py").read())
        studnum = re.search(r'\d+', re.search(r'student=\d+\">\[19\]', lab3).group(0)).group(0)
        for i in self.spisok:
            i.peredacha(studnum)
            print(i)
            
    
    def readfile(self):
        s = open(group.Gubkin,"rb")
        self.spisok = pickle.load(s)
        return self.spisok
