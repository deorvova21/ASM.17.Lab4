import urllib.request, urllib.parse, re
from .Undergraduate import *

class Group:
    def __init__(self):
        self.group = []
        res = urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py")
        page = str(res.read())
        res = re.search('\d+">\[07\]', page).group(0)
        sid = re.search('\d+', res).group(0)
        self.url = 'http://localhost:81/cgi-bin/lab3.py?student=' + sid

    def AddStudent(self):
        student = Student()
        q = '&act=get&id=addstudent&' + urllib.parse.urlencode(student.Edit())
        urllib.request.urlopen(self.url + q)
        print()

    def AddUndergraduate(self):
        elder = Undergraduate()
        q = '&act=get&id=addundergraduate&' + urllib.parse.urlencode(elder.Edit())
        urllib.request.urlopen(self.url + q)
        print()

    def ShowList(self):
        q = '&act=display'
        res = urllib.request.urlopen(self.url + q)
        page = res.read().decode()
        print('-Список студентов-')
        print(page)

    def ChangeStudent(self):
        sid = input('Введите ID записи для редактирования: ')
        q = '&act=edit&id=' + sid
        res = urllib.request.urlopen(self.url + q)
        page = str(res.read())
        if page == str(b'\n'):
            print('Неверный ввод')
            self.edit()
            return
        else:
            try:
                re.search('advisor', page).group(0)
                student = Undergraduate()
            except:
                student = Student()
            q = '&act=get&id={}&{}'.format(sid, urllib.parse.urlencode(student.Edit()))
            urllib.request.urlopen(self.url + q)

    def WriteToFile(self):
        q = '&act=savebin'
        urllib.request.urlopen(self.url + q)
        print('Список сохранен в файл file.dat\n')

    def ReadFromFile(self):
        q = '&act=loadbin'
        urllib.request.urlopen(self.url + q)
        print('Список загружен из файла file.dat\n')

    def ClearList(self):
        q = '&act=clear'
        urllib.request.urlopen(self.url + q)
        print('Список очищен\n')

    def DeleteStudent(self):
        sid = input('Введите ID записи для удаления: ')
        q = '&act=delete&id=' + sid
        res = urllib.request.urlopen(self.url + q)
        print('Студент удален')
