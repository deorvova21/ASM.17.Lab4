import pickle, os
from .category import *
from .dish import *
import urllib.request
import re

class Items:
    def __init__(self):
        self.l=list()
        
    def read_file(self):
        if (os.path.exists("st18/file.dat")):
            self.l = pickle.load(open("st18/file.dat", "rb"))
            print("Список считан!")
        else:
            print("Ошибка чтения файла!")

    def send(self):
        if (len(self.l)==0):
            print("Список пуст!")
            return
        rec = str((urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py")).read())
        result = re.search(r'student=\d+\">\[18\]', rec).group(0)
        result = re.search(r'\d+', result).group(0)
        id=0
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?student="+result+"&action=6")
        for o in self.l:
            rec = o.send()
            if type(o) is Dish: stype="2"
            else: stype="1"
            urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?student="+result+"&action=7&id="+str(id)+"&stype="+stype+"&"+rec)
            id+=1
        print("Данные переданы на сервер")



    

    
