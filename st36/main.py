from .autocenter import *

autocenter = Autocenter()

menu = {"1": ("Send", autocenter.send),
        "2": ("Exit", "")}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
            
        user_input = input("")
        if int(user_input) == 2:
            break
        menu[user_input][1]()
