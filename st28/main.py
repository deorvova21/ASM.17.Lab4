import pickle
import re
import urllib

from .ModelSender import ModelSender

URL = 'http://localhost:81/cgi-bin/lab3.py'
FILENAME = 'st28/agency.dat'


def find_student_id():
    my_number = 28
    data = str(urllib.request.urlopen(URL).read())
    id = re.search(r'student=(\d+)\">\[' + str(my_number) + '\]', data).group(1)
    return id


def read_agency_from_file(filename):
    with open(filename, 'rb') as f:
        agency = pickle.load(f)
        f.close()
    return agency


def main():
    params = {'student': find_student_id(),
              'model_id': -1,
              'action': 'save_model'}
    agency = read_agency_from_file(FILENAME)
    ModelSender(URL, params).send(agency)
