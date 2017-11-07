import os
import pickle
from .HttpCarImporter import HttpCarImporter
from .Finder import Finder


def main():
    server_url = "http://localhost:81/cgi-bin/lab3.py"
    student_id = 26
    dump_file_path = os.path.dirname(os.path.abspath(__file__)) + '\\storage\\dump'

    print('getting student number...')
    finder = Finder(server_url)
    student_num = finder.find_student_num(student_id)
    print('student number: ' + student_num)

    additional_params = {
        'student': student_num,
        'route': 'car/store'
    }

    f = open(dump_file_path, 'rb')
    data = pickle.load(f)
    f.close()

    importer = HttpCarImporter(server_url)
    importer.send_to_server(data, additional_params)
