from .warrior import *


class Mage(Warrior):
    
    def __init__(self):
        super().__init__()
        self.mana = ""
        self.spell = ""


    def send(self):
        warInf = "&name="+urq.quote(self.name)+"&health="+urq.quote(self.health)+"&attack="+urq.quote(self.attack)+"&mana="+urq.quote(self.mana)+"&spell="+urq.quote(self.spell)
        return warInf
