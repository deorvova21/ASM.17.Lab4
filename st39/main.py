from .Util import Util
import pickle


URL = 'http://localhost:81/cgi-bin/lab3.py'
DUMP = 'st39/dump.pkl'
ABS_NUMBER = 39


def main():
    u = Util(URL, ABS_NUMBER)
    staff = None
    with open(DUMP, 'rb') as f:
        print("File dump is ready to be sent: ", DUMP)
        staff = pickle.load(f)

    for i, person in enumerate(staff):
        u.send_person(person)
        print('{0} of {1} records sent'.format(i+1, len(staff)))

    print("Done")





