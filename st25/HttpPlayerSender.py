from urllib.request import urlopen
from urllib.parse import urlencode
import re


class HttpPlayerSender:
    def __init__(self, server_url):
        self.__server_url = server_url

    def get_student_index(self):
        content = str(urlopen(self.__server_url).read())
        id_in_list = 25
        return re.search(r'student=(\d+)\">\[' + str(id_in_list) + '\]', content).group(1)

    def send(self, container):
        print('Sending...')

        index = self.get_student_index()
        tmp = {'student': index, 'player_id': -1, 'action': 'save_player'}
        const_url_part = self.__server_url + '?' + urlencode(tmp) + '&'
        for player in container:
            request = const_url_part + urlencode(player.get_fields_dictionary())
            print(str(player) + ' is sending...')
            try:
                urlopen(request)
            except:
                print('Error!')
        print('Done!')