import urllib.request as urq

class Warrior:

    def __init__(self):
        self.id = ""
        self.name = ""
        self.health = ""
        self.attack = ""


    def send(self):
        warInf = "&name="+urq.quote(self.name)+"&health="+urq.quote(self.health)+"&attack="+urq.quote(self.attack)+"&action=6"  
        return warInf
    
