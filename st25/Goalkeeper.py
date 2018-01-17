from .Player import Player

class Goalkeeper(Player):
    __reaction: int = 0

    def __init__(self, playername, raiting, reaction):
        super().__init__(playername, raiting)
        self.__reaction = reaction

    def get_fields_dictionary(self):
        tmp = super().get_fields_dictionary()
        tmp.update({'is_goalkeeper': 1})
        tmp.update({'reaction': self.__reaction})
        return tmp

    def __str__(self):
        return 'Playername = {0}, Raiting = {1}, Reaction = {2}'\
            .format(self._playername, self.raiting, self.__reaction)