from .HttpPlayerSender import HttpPlayerSender
import pickle, os

def main():
    url = 'http://localhost:81/cgi-bin/lab3.py'
    sender = HttpPlayerSender(url)

    container_file_path = os.path.dirname(os.path.abspath(__file__)) + '\\container.pkl'

    with open(container_file_path, 'rb') as f:
        container = pickle.load(f)
        f.close()

    sender.send(container)