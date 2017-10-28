import pickle

from .Loader import Loader


def main():
    student_id = input('student id lab3...\n')
    loader = Loader(student_id)
    with open('st22/store/storage', 'rb') as f:
        people = pickle.load(f)
        for man in people:
            loader.send(man)
