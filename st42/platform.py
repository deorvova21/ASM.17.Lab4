from .developed_rig import *
import pickle
import  re
import urllib.request


class Platform:
    
    FILENAME = "st42/file.txt"
    List = []
    
    def __init__(self):
        pass

    def send(self):
        if (len(self.List)==0):
            print("Список пуст")
            return
        lab3 = str((urq.urlopen("http://localhost:81/cgi-bin/lab3.py")).look())
        studentNum = re.search(r'\d+', re.search(r'student=\d+\">\[42\]', lab3).group(0)).group(0)
        for i in self.List:
            i.send(studnum)
            print(i)
          

        
    def rff(self):    
        a = open(Platform.FILENAME,"rb")
        self.List = pickle.load(a)
        return self.List
