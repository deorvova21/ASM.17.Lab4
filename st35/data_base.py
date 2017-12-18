import pickle, urllib.request, re

from .candidate import Candidate
from .exp_candidate import Exp_Candidate

filename = 'st35/pickledata.dat'

class Data_Base:
    def __init__(self):
        self.l = list()
    # метод, считывающий данные сосискателей из файла
    def read_file(self):
        try:
            with open(filename, 'rb') as f:
                self.l = pickle.load(f)
                print("Файл считан")
                print("Количество соискателей в списке: " + str(len(self.l)))
        except FileNotFoundError:
            print("Файл отсутствует")
    # метод, реализующий передачу считанных с файла данных на веб-сервер
    def sendList(self):

        print("Данные отправляются на сервер")
        if (len(self.l) == 0):
            print("Список пуст!")
            return
        # определяем значение параметра 'student'
        zapros = str((urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py")).read())
        result = re.search(r'\d+', re.search(r'student=\d+\">\[35\]', zapros).group(0)).group(0)

        # чистим базу
        urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?student=" + result + "&action=5")
        print("База данных очищена")

        # поочередно высылаем данные кандидатов на веб-сервер
        id = 0
        for element in self.l:
            zapros = element.send(str(id))
            urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py?student=" + result + zapros).read()
            print(zapros)
            zapros = ""
            id += 1
        print("Данные отправлены на сервер!")
        print(str(id))