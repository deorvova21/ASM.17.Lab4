from .Sender import Sender
import pickle


def main():
    file_path = "st34/Storage/container.pkl"
    url = 'http://localhost:81/cgi-bin/lab3.py'

    with open(file_path, 'rb') as f:
        container = pickle.load(f)
        f.close()

    student_number = 34
    Sender(url, student_number).send_container(container)
