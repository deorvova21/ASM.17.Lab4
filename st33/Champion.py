from .Sportsman import *


class Champion(Sportsman):
    def __init__(self):
        super().__init__()
        self._wins = None

    def getWins(self):
        return self._wins