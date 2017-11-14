from .HttpAnimalSender import HttpAnimalSender
import pickle, os

def main():
    url = 'http://localhost:81/cgi-bin/lab3.py'
    sender = HttpAnimalSender(url)

    zoo_file_path = os.path.dirname(os.path.abspath(__file__)) + '\\Storage\\zoo.pkl'

    with open(zoo_file_path, 'rb') as f:
        zoo = pickle.load(f)
        f.close()

    sender.send(zoo)
