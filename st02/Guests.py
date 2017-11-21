import pickle

class Guest(object):
    def __init__(self):
        self.name = None
        self.surname = None
        
    def __str__(self):
        res = "Name: " + self.name +\
              "\nSurname: " + self.surname
        return res
        
