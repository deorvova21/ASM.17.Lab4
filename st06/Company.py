import urllib.request, urllib.parse, re
from .Fired import *

class Company:
    def __init__(self):
        self.company = []
        res = urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py")
        page = str(res.read())
        res = re.search('\d+">\[06\]', page).group(0)
        wid = re.search('\d+', res).group(0)
        self.url = 'http://localhost:81/cgi-bin/lab3.py?student=' + wid

    def Add_Worker(self):
        worker = Worker()
        q = '&act=get&act2=Worker&' + urllib.parse.urlencode(worker.Edit_Show())
        urllib.request.urlopen(self.url + q)
        print()

    def Add_Fired(self):
        worker = Fired()
        q = '&act=get&act2=Fired&' + urllib.parse.urlencode(worker.Edit_Show())
        print(self.url + q)
        urllib.request.urlopen(self.url + q)
        print()

    def Show_List(self):
        q = '&act=show'
        res = urllib.request.urlopen(self.url + q)
        page = res.read().decode()
        print('Каталог')
        print(page)

    def Edit_Worker(self):
        wid = input('Введите ID записи для редактирования: ')
        q = '&act=edit&wid=' + wid
        res = urllib.request.urlopen(self.url + q)
        page = str(res.read())
        if page == str(b'\n'):
            print('Неверный ввод')
            self.edit()
            return
        else:
            try:
                re.search('reason', page).group(0)
                worker = Fired()
            except:
                worker = Worker()
            q = '&act=get&act2=edit&wid={}&{}'.format(wid, urllib.parse.urlencode(worker.Edit_Show()))
            urllib.request.urlopen(self.url + q)

    def Write_File(self):
        q = '&act=save'
        urllib.request.urlopen(self.url + q)

    def Read_File(self):
        q = '&act=load'
        urllib.request.urlopen(self.url + q)

    def Clear_List(self):
        q = '&act=clear'
        urllib.request.urlopen(self.url + q)
        print('Список очищен\n')

    def Delete_Worker(self):
        wid = input('Введите номер работника: ')
        q = '&act=delete&wid=' + wid
        res = urllib.request.urlopen(self.url + q)
        print('Удаление выполнено')
