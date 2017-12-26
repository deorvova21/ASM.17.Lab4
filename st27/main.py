import pickle
import re
import urllib

from .SendSbornik import SendSbornik

URL = 'http://localhost:81/cgi-bin/lab3.py'
FILENAME = 'st27/eLibrary.dat'


def find_student_id():
    _id = 27
    data = str(urllib.request.urlopen(URL).read())
    id = re.search(r'student=(\d+)\">\[' + str(_id) + '\]', data).group(1)
    return id


def read_from_file(filename):
    with open(filename, 'rb') as f:
        library = pickle.load(f)
        f.close()
    return library


def main():
    params = {'student': find_student_id(),
              'sbornik_id': -1,
              'action': 'save_sbornik'}
    library = read_from_file(FILENAME)
    SendSbornik(URL, params).send(library)
