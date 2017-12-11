from .Guests import *
#import Guests

class Registered(Guest):
    def __init__(self):
        super().__init__()
        self.number = None

    def __str__(self):
        res = super().__str__() + "\nNumber: " + str(self.number)
        return res
    

