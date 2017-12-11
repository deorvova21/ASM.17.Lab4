from .transfer import *

url = 'http://localhost:81/cgi-bin/lab3.py'
FILENAME = "st21/storage.pkl"
transfer = Transfer(url, FILENAME)


def main():
    transfer.send_data()

