import urllib.request
from .category import *

class Dish(Category):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.price = ""
        self.weight= ""

    def send(self):
        rec=Category.send(self)
        rec=rec+"&name="+urllib.request.quote(self.name)+"price="+urllib.request.quote(self.price)+"weight="+urllib.request.quote(self.weoght)
        return rec
    
    
