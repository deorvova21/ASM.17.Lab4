from .fullinfcar import *
import pickle
import  re


class autopark:
    
    FILENAME = "st18/file.txt"
    List = []
    
    def __init__(self):
        pass

    def send(self):
        self.rff()
        if (len(self.List)==0):
            print("List is empty")
            return
        lab3 = str((urq.urlopen("http://localhost:81/cgi-bin/lab3.py")).read())
        studentNum = re.search(r'\d+', re.search(r'student=\d+\">\[36\]', lab3).group(0)).group(0)
        for i in self.List:
            autoInf = i.send()
            print(autoInf)
            urq.urlopen("http://localhost:81/cgi-bin/lab3.py?index=-1&id=&student=" + studentNum + autoInf)

        
    def rff(self):
        pickle_in = open(autopark.FILENAME,"rb")
        self.List = pickle.load(pickle_in)
    


