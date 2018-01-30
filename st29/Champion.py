from .Sportsman import *


class Champion(Sportsman):
    def __init__(self):
        super().__init__()
        self._wins = None

    def getWins(self):
        return self._wins

    
    def send():
        return  "&full_name="+ urllib.parse.quote(str(e.getFull_name())) + "&age=" + urllib.parse.quote(str(e.getAge())) + "&rating="+ urllib.parse.quote(str(e.getRating())) + "&wins=" + urllib.parse.quote(str(e.getWins()))
