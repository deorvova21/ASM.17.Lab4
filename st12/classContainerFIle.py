from .descendantClassFile import descendantClass
from .myClassFile import myClass
import pickle,re
import urllib.request as urq

class classContainer:

    def __init__(self,):
        self.classList = list()


    def importFromPickle(self):
        filename="st12/1.txt"
        with open(filename, "rb") as file:
            self.classList = pickle.load(file)

        lab3url = str((urq.urlopen("http://localhost:81/cgi-bin/lab3.py")).read())
        myNymber = re.search(r'\d+', re.search(r'student=\d+\">\[12\]', lab3url).group(0)).group(0)
        print("Мой номер:{0}".format(myNymber))
        for i in range(0, len(self.classList)):
            self.classList[i].addInBase(myNymber)

