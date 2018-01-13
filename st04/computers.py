import pickle, copy, os
from .computer_case import Computer_case
from .notebook import Notebook
import urllib.request
import urllib.parse


class Computers:
    def __init__(self):
        self.l=list()
        
    def read_file(self):
        if (os.path.exists("st04/file.dat")):
            self.l = pickle.load(open("st04/file.dat", "rb"))
            print("Read list!")
        else:
            print("File not found!")

    def server(self):
        f = urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py")
        text = str(f.read())
        kol = len(text)
        i=kol-4
        k1=-1
        k2=-1
        while (i!=0):
            if (text[i]=='[') and (text[i+1]=='0') and (text[i+2]=='5') and (text[i+3]==']'):
                k1=1
            if (text[i]=='"'):
                if (k1==1) and (k2!=-1):
                    k1=i+1
                    break
                if (k1==1): k2=i
            i+=-1
        text=text[k1:k2]
        kol = len(self.l)
        if (kol!=0):
            f = urllib.request.urlopen("http://localhost:81"+text+"&action=5")
            f.read()
            k=0
            for o in self.l:
                if type(o) is Computer_case: i=1
                else: i=2
                mes=o.write()
                mes.append(["add",i])
                mes=dict(mes)
                enc_data = urllib.parse.urlencode(mes)
                k+=1
                f = urllib.request.urlopen("http://localhost:81"+text+"&action=6&"+enc_data)
                f.read()
            print("Ok")
        else:
            print("the list is empty")



        
    

    
