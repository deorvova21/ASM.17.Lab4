from .car import *


class Supercar(Car):
    
    def __init__(self):
        super().__init__()
        self.nitro = ""
        self.modification = ""


    def send(self):
        autoInf = "&model="+urq.quote(self.model)+"&type="+urq.quote(self.type)+"&color="+urq.quote(self.color)+"&nitro="+urq.quote(self.nitro)+"&modification="+urq.quote(self.modification)+"&action=7"
        return autoInf
