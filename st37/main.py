from .dinner import *

dinner = dinner()

menu = {"1": ("Чтение из файла", dinner.readfile),
        "2": ("Отправить", dinner.send),
        "3": ("Выход", "")}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])  
        deystvie= input()
        if int(deystvie) == 3:
            break
        menu[deystvie][1]()
