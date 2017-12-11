from .Util import Util
import pickle


URL = 'http://localhost:81/cgi-bin/lab3.py'
DUMP = 'st09/dump.pkl'
ABS_NUMBER = '09'


def main():
    u = Util(URL, ABS_NUMBER)
    lst = None
    with open(DUMP, 'rb') as f:
        print("File dump is ready to be sent: ", DUMP)
        lst = pickle.load(f)

    for i, market in enumerate(lst):
        u.send_market(market)
        print('{0} of {1} records sent'.format(i+1, len(lst)))

    print("Done")





