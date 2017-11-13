import urllib.request, urllib.parse, re
from .used import *

class Catalog:
    def __init__(self):
        self.catalog = []
        res = urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py")
        page = str(res.read())
        res = re.search('\d+">\[24\]', page).group(0)
        sid = re.search('\d+', res).group(0)
        self.url = 'http://localhost:81/cgi-bin/lab3.py?student=' + sid

    def add_new(self):
        auto = Auto()
        q = '&act=get&act2=new&' + urllib.parse.urlencode(auto.edit())
        urllib.request.urlopen(self.url + q)
        print()

    def add_used(self):
        auto = Used()
        q = '&act=get&act2=used&' + urllib.parse.urlencode(auto.edit())
        print(self.url + q)
        urllib.request.urlopen(self.url + q)
        print()

    def show_catalog(self):
        q = '&act=show'
        res = urllib.request.urlopen(self.url + q)
        page = res.read().decode()
        print('Каталог')
        print(page)

    def edit_catalog(self):
        sid = input('Введите ID записи для редактирования: ')
        q = '&act=edit&cid=' + sid
        res = urllib.request.urlopen(self.url + q)
        page = str(res.read())
        if page == str(b'\n'):
            print('Неверный ввод')
            self.edit()
            return
        else:
            try:
                re.search('mileage', page).group(0)
                auto = Used()
            except:
                auto = Auto()
            q = '&act=get&act2=edit&cid={}&{}'.format(sid, urllib.parse.urlencode(auto.edit()))
            urllib.request.urlopen(self.url + q)

    def save_catalog(self):
        q = '&act=savedat'
        urllib.request.urlopen(self.url + q)

    def load_catalog(self):
        q = '&act=loaddat'
        urllib.request.urlopen(self.url + q)

    def clear_catalog(self):
        q = '&act=clear'
        urllib.request.urlopen(self.url + q)
        print('Каталог очищен\n')

    def delete_auto(self):
        sid = input('Введите ID записи для удаления: ')
        q = '&act=delete&cid=' + sid
        res = urllib.request.urlopen(self.url + q)
        print('Автомобиль удален')
