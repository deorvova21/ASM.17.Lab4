from .squad import *

squad = Squad()

menu = {"1": ("Отправить", squad.send),
        "2": ("Выход", "")}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
            
        user_input = input("")
        if int(user_input) == 2:
            break
        menu[user_input][1]()
