import sys, pickle, os, cgi, re
import urllib.request
import urllib.parse
from .Driver import *

class Car_company:
    def __init__(self):
        self.spisok=[]
        self.number=''
        
    def loading(self):
        if os.path.exists("st18/file.dat"):
            self.spisok=pickle.load(open("st18/file.dat", "rb"))
            print("Done")
        else:
            print('error')

    def connection(self):
        res=urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py")
        data=str(res.read())
        self.number = re.search(r'student=(\d+)\">\[12\]', data).group(1)
        
    def store(self):
        self.connection()
        for item in self.spisok:
            fi=urllib.parse.urlencode(item.write())
            if type(item) is Car: 
                res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number)+'&tip=car&type=add_stu&i=None&' + fi)
            else:
                res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number)+'&type=add_sta&tip=driver&i=None&' + fi)
            res.read()
        print('Done\n')

    def delete(self):
        self.connection()
        res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number)+'&type=dell_all')
        print('Done')

    def add_stu(self):
        car=Car()
        car.edit()
        fi=urllib.parse.urlencode(car.write())
        self.connection()
        res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number)+'&tip=car&type=add_stu&i=None&'+fi)
        print('Done')

    def add_sta(self):
        driver=Driver()
        driver.edit()
        fi=urllib.parse.urlencode(driver.write())
        self.connection()
        res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number)+'&tip=driver&type=add_sta&i=None&'+fi)
        print('Done')
        
    def show(self):
        self.connection()
        res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number))
        t=res.read()
        h=t.decode()
        g=re.sub('<br>\n', ' ', h)
        result=re.findall( r'Name: \w+.\w+..\w+.\w+..\w+.\w+.\w+......\w+.\w+......\w+..\w+..\w+.\w+.\w+..\w+',g)
       
        for item in result:
            print(item)

    def dell(self):
        self.connection()
        self.show()
        i=input('Enter number: ')
        res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number)+'&type=dell&i='+i)
        print(i)
    
    def change(self):
        self.connection()
        self.show()
        i=input('Enter number: ')
        kind=input('type (car or driver: ')
        if kind=='car':
            car=Car()
            car.edit()
            fi=urllib.parse.urlencode(car.write())
            res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number)+'&tip=car&type=edit&i='+i+'&'+fi)
            print('Done')
        elif kind=='driver':
            driver=Driver()
            driver.edit()
            fi=urllib.parse.urlencode(driver.write())
            res=urllib.request.urlopen('http://localhost:81/cgi-bin/lab3.py?student='+str(self.number)+'&tip=driver&type=edit&i='+i+'&'+fi)
            print('Done')
        else:
            print('Error')
            
        
        
        
        
        
        
