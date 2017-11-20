
from .sportclub import *

def load(sportclub):
    sportclub.load()
    print("Uploaded\n")

def send(sportclub):
    sportclub.send()
    print("Sent\n")

def exit(sportclub):
    return

sportclub = Sportclub()

def main():    
    print("Menu")
    print("1. Load from file")    
    print("2. Send to http")
    print("0. Exit")
    choice = input(" >>  ")
    menu(choice)

def menu(choice):
    try:
        menu_actions[choice](sportclub)
    except KeyError:
        print("Error\n")
    if choice != '0':       
        menu_actions['main']()


menu_actions = {
    'main': main,
    '1': load,
    '2': send,
    '0': exit,
}
 
if __name__ == "__main__":
    main()
