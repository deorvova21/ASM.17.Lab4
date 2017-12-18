from .data_base import *

def main():
        data_base = Data_Base()

        list = [
	["Считать список из файла", data_base.read_file],
        ["Отправить данные на сервер", data_base.sendList],
	]

        try:
                while True:
                        i = 1
                        print("Выбрать")
                        for o in list:
                                print(i, o[0])
                                i += 1
                        print("Нажмите любую клавишу для выхода\n")
                        k = int(input())
                        print("------------------------------")
                        list[k-1][1]()
                        print("------------------------------")
        except:
                print("bye")
