from .mage import *
import pickle
import  re


class Squad:
    
    FILENAME = "st05/file.txt"
    List = []
    
    def __init__(self):
        pass

    def send(self):
        self.rff()
        if (len(self.List)==0):
            print("Список пуст")
            return
        lab3 = str((urq.urlopen("http://localhost:81/cgi-bin/lab3.py")).read())
        studentNum = re.search(r'\d+', re.search(r'student=\d+\">\[05\]', lab3).group(0)).group(0)
        for i in self.List:
            warInf = i.send()
            print(warInf)
            urq.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&id=&student=" + studentNum + warInf)

        
    def rff(self):
        pickle_in = open(Squad.FILENAME,"rb")
        self.List = pickle.load(pickle_in)
    


