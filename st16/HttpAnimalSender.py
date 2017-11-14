from urllib.request import urlopen
from urllib.parse import urlencode
import re


class HttpAnimalSender:
    def __init__(self, server_url):
        self.__server_url = server_url

    def get_student_index(self):
        content = str(urlopen(self.__server_url).read())
        id_in_list = 16
        return re.search(r'student=(\d+)\">\[' + str(id_in_list) + '\]', content).group(1)

    def send(self, zoo):
        print('Sending...')

        index = self.get_student_index()
        tmp = {'student': index, 'animal_id': -1, 'action': 'save_animal'}
        const_url_part = self.__server_url + '?' + urlencode(tmp) + '&'
        for animal in zoo:
            request = const_url_part + urlencode(animal.get_fields_dictionary())
            print(str(animal) + ' is sending...')
            try:
                urlopen(request)
            except:
                print('Error!')
        print('Done!')
