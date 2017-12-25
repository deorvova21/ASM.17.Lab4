import pickle

from .Loader import Loader


def main():
    student_id = input('Enter Person id from ASM.17.Lab3...\n')
    loader = Loader(student_id)
    with open('st13/store/storage', 'rb') as f:
        people = pickle.load(f)
        for man in people:
            loader.send(man)
