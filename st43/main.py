from .Devices import *

dev = Devices()
menu = {"1": ("Read file data", dev.read_file),
        "2": ("Send data to server", dev.send),
        "3": ("Exit", "")}


def main():
    while True:
        for key in menu:
            print(key + ": " + menu[key][0])
        act = input()
        if int(act) == 3:
            break
        menu[act][1]()
