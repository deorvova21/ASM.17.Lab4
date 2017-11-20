from urllib.request import urlopen
from urllib.parse import urlencode
import re
import os
import pickle


def main():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '\\mobile_phone_shop.dat', 'rb')
    phones = pickle.load(f)

    base_url = "http://localhost:81/cgi-bin/lab3.py"
    print('getting student number from: ' + base_url)
    content = str(urlopen(base_url).read())
    student_num = re.search(r'student=(\d+)\">\[' + str(10) + '\]', content).group(1)
    print('student number is ' + student_num)

    for phone in phones:
        data = phone.get_data()
        type = data.get('type')

        action = None
        if type == 'mobile_phone':
            action = 'insert_mobile_phone'
        elif type == 'smart_phone':
            action = 'insert_smart_phone'

        params = {**data, **{
            'student': student_num,
            'action': action
        }}

        import_url = base_url + '?' + urlencode(params)
        print('sending request to url: ' + import_url)
        urlopen(import_url)
