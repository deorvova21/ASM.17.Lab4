import urllib.request as urq

class Car:

    def __init__(self):
        self.id = ""
        self.model = ""
        self.type = ""
        self.color = ""


    def send(self):
        autoInf = "&model="+urq.quote(self.model)+"&type="+urq.quote(self.type)+"&color="+urq.quote(self.color)+"&action=6"  
        return autoInf
    
