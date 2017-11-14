import os, pickle

from .Loader import Loader

STORAGE_FILENAME = 'st99/journal.dat'
STUDENT_NUMBER = 99 

def main():
    loader = Loader(STUDENT_NUMBER)
    
    runs = []
    if os.path.getsize(STORAGE_FILENAME) > 0:
        print("Начинаем загрузку...")
        with open(STORAGE_FILENAME, 'rb') as f:
            unpickler = pickle.Unpickler(f)
            runs = unpickler.load()
        for run in runs:
            loader.load(run)
    else:
        print("В папке нет нужного файла или файл пуст.")
