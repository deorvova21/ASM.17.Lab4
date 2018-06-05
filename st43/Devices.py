from .Smartphone import *
import pickle
import re
import urllib.request


class Devices:
    def __init__(self):
        self.dev_list = []
        self.dev_file = './st43/dev_list.pkl'

    def send(self):
        if (len(self.dev_list) == 0):
            print("List is empty!\n")
            return
        lab3 = str(urllib.request.urlopen("http://localhost:81/cgi-bin/lab3.py").read())
        obj = re.search(r'\d+', re.search(r'student=\d+\">\[43\]', lab3).group(0)).group(0)
        for el in self.dev_list:
            el.put(obj)
            print(el)

    def read_file(self):
        f = open(self.dev_file, "rb")
        self.dev_list = pickle.load(f)
        return self.dev_list
        print("Done!\n")
