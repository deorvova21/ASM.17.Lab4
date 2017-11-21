from .overseer import *
import pickle
import urllib.parse
import urllib.request
import os
import re


def spec_to_hex(data, range_):
    string = ''
    for i in range(range_):
        lst = list(data[i])
        for ind, item in enumerate(lst):
            if 32 <= ord(item) <= 47 or 58 <= ord(item) <= 64 or 91 <= ord(item) <= 96:
                lst[ind] = '%' + hex(ord(item))
            string += lst[ind]
        string += ' '
    return string.split()


class Transfer:
    
    def __init__(self, url, filename):
        self.url = url
        self._stack = []
        self.filename = filename

    def read_from_file(self):
        try:
            os.path.exists(self.filename)
            self._stack = pickle.load(open(self.filename, 'rb'))
        except FileNotFoundError:
            return 0
        else:
            return 1

    def send_data(self):
        print('Sending data...')
        if self.read_from_file() != 0:
            data = []
            try:
                main_page = str((urllib.request.urlopen(self.url)).read())
                st_id = re.search(r'student=(\d+)\">\[21\]', main_page).group(1)
                for ind, item in enumerate(self._stack):
                    item.output_data(data)
                    if len(data) == 3:
                        string = spec_to_hex(data, 3)
                        #urllib.request.urlopen(self.url + '?student={}&action=edit_stack&add=prisoner'.format(st_id))
                        urllib.request.urlopen(self.url + '?student={0}&action=edit_stack&add=prisoner&f_name={1}&l_name={2}&age={3}'
                                               .format(st_id, string[0], string[1], string[2]))
                        print(string)
                    else:
                        string = spec_to_hex(data, 5)
                        #urllib.request.urlopen(self.url + '?student={}&action=edit_stack&add=overseer'.format(st_id))
                        urllib.request.urlopen(self.url + '?student={0}&action=edit_stack&add=overseer&f_name={1}'
                                                          '&l_name={2}&age={3}&salary={4}&phone_numb={5}'
                                               .format(st_id, string[0], string[1], string[2], string[3], string[4]))
                        print(string)
            except urllib.error.URLError:
                print('URLError')
            except urllib.error.HTTPError:
                print('HTTPError')
            else:
                print('Done.')
        else:
            print('Failed to open file')



