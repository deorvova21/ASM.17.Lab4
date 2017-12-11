from urllib.request import urlopen
from urllib.parse import urlencode
import re
import os
import pickle


def main():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '\\file.txt', 'rb')
    persons = pickle.load(f)
    f.close()

    content = str(urlopen("http://localhost:81/cgi-bin/lab3.py").read())
    student = re.search(r'student=(\d+)\">\[' + str(38) + '\]', content).group(1)

    print('student: ' + student)

    url = "http://localhost:81/cgi-bin/lab3.py"
    for person in persons:
        params = {}
        if person.type == 'employee':
            params = {
                'student': student,
                'action': 6,
                'index': '8',
                'type': person.type,
                'name': person.name,
                'age': person.age,
                'start': person.start,
                'salary': person.salary
            }
        elif person.type == 'developer':
            params = {
                'student': student,
                'action': 7,
                'index': '8',
                'type': person.type,
                'name': person.name,
                'age': person.age,
                'start': person.start,
                'salary': person.salary,
                'language': person.language,
                'exp': person.exp
            }
        person_add_url = url + '?' + urlencode(params)
        print(person_add_url)
        urlopen(person_add_url)
