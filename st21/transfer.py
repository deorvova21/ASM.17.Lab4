from .overseer import *
import pickle
import urllib.parse
import os
import re


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
        if self.read_from_file():
            try:
                main_page = str((urllib.request.urlopen(self.url)).read())
                st_id = re.search(r'student=(\d+)\">\[21\]', main_page).group(1)
                for ind, item in enumerate(self._stack):
                    item.send_data(self.url, st_id)
            except urllib.error.URLError:
                print('URLError')
            else:
                print('Done.')
        else:
            print('Failed to open file')



