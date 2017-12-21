import pickle

from .Loader import Loader


def main():
    person_id = input('person id lab3...\n')
    loader = Loader(person_id)
    with open('st13/store/storage', 'rb') as f:
        people = pickle.load(f)
        for man in people:
            loader.send(man)
