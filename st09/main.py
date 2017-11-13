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
    student = re.search(r'student=(\d+)\">\[' + str(09) + '\]', content).group(1)

    print('student: ' + student)

    url = "http://localhost:81/cgi-bin/lab3.py"
    for head in heads:
        params = {}
        if head.type == 'department':
            params = {
                'student': student,
                'action': 6,
                'index': 'add',
                'type': head.type,
                'nickname': head.nickname,
                'owner_name': head.owner_name,
                'product_type': head.product_type,
                'address': head.address
            }
        elif head.type == 'seller':
            params = {
                'student': student,
                'action': 7,
                'index': 'add',
                'type': head.type,
                'nickname': head.nickname,
                'owner_name': head.owner_name,
                'product_type': head.product_type,
                'address': head.address
                'name_seller': head.name_seller,
                'tel': head.tel
            }
        head_add_url = url + '?' + urlencode(params)
        print(head_add_url)
        urlopen(head_add_url)
