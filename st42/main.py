from .quiz import *
import pickle


URL = 'http://localhost:81/cgi-bin/lab3.py'
DUMP = 'st42/dump.pkl'
ABS_NUMBER = 42


def main():
    u = Quiz(URL, ABS_NUMBER)
    thing = None
    with open(DUMP, 'rb') as f:
        print("Файл готов к отправке: ", DUMP)
        thing = pickle.load(f)

    for i, person in enumerate(thing):
        u.send_person(person)
        print('{0} of {1} отправлен'.format(i+1, len(thing)))

    print("Done")





