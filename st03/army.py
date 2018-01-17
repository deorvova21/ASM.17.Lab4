from .Soldier import *
from .Mercenary import *
import pickle, urllib.parse, urllib.request, re

class Staff:
    def __init__(self):
        self.l = []

    def read(self):
        with open('st03/staff.dat', 'rb') as f:
            self.l = pickle.load(f)
            print ("Success")


    def write(self):
        idd = self.id_student()
        print ('Student #:', idd)
        for item in self.l:
            dict_item = {'student' : idd, 'action' : '7', 'class' : '1', 'save' : '1', 'edit' : '-1', 'name' : item.name, 'surname' : item.surname, 'age' : item.age, 'specialization' : item.specialization}
            if type(item) == Officer:
                dict_item['save'] = '2'
                dict_item['rank'] = item.rank
                dict_item['salary'] = item.salary
            urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?' + urllib.parse.urlencode(dict_item))
        print ('Отправлено')

    def id_student(self):
        idd = re.search('<a href=\"\/cgi-bin\/lab3\.py\?student=(\d)\">\[02\]',str(urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py').read())).group(1)
        return idd
        
