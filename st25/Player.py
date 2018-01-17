class Player:
    _playername: str = ''
    _raiting: int = 0

    def __init__(self, playername, raiting):
        self._playername = playername
        self._raiting = raiting

    def get_fields_dictionary(self):
        return {'playername': self._playername, 'raiting': self._raiting, 'is_goalkeeper': 0}

    def __str__(self):
        return 'Playername = {0}, Raiting = {1}' \
            .format(self._playername, self._raiting)