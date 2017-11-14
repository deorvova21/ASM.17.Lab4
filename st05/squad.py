from .mage import *
import pickle
import  re


class Squad:
    
    FILENAME = "st05/file.txt"
    spisok = []
    
    def __init__(self):
        pass

    def send(self):
        self.rff()
        if (len(self.spisok)==0):
            print("Список пуст")
            return
        lab3 = str((urq.urlopen("http://localhost:81/cgi-bin/lab3.py")).read())
        studentNum = re.search(r'\d+', re.search(r'student=\d+\">\[05\]', lab3).group(0)).group(0)
        for i in self.spisok:
            warInf = i.send()
            print(warInf)
            if type(i) is Warrior:
                urq.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + studentNum + warInf + "&action=6")
            else:
                urq.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&student=" + studentNum + warInf + "&action=7")
        
    def rff(self):
        pickle_in = open(Squad.FILENAME,"rb")
        self.spisok = pickle.load(pickle_in)
    


