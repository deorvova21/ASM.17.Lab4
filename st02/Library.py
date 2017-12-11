from .Guests import *
from .Registered import *
import pickle, urllib.parse, urllib.request, re

class Library:
    def __init__(self):
        self.l = []

    def read(self):
        with open('st02/file.db', 'rb') as f:
            self.l = pickle.load(f)
            print ("Success")

##        for item in self.l:
##            print (item)

    def write(self):
        idd = self.id_student()
        print ('Student #:', idd)
        for item in self.l:
            dict_item = {'student' : idd, 'id' : '-1', 'act' : 'save_guest', 'obj' : '1', 'name' : item.name, 'surname' : item.surname}
            if type(item) == Registered:
                dict_item['act'] = 'save_reg'
                dict_item['obj'] = '2'
                dict_item['number'] = item.number
            urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?' + urllib.parse.urlencode(dict_item))
        print ('Отправлено')

    def id_student(self):
        idd = re.search('<a href=\"\/cgi-bin\/lab3\.py\?student=(\d)\">\[02\]',str(urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py').read())).group(1)
        return idd
        
