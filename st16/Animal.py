class Animal:
    _nickname: str = ''
    _limbs_count: int = 0

    def __init__(self, name, limbs_count):
        self._nickname = name
        self._limbs_count = limbs_count

    def get_fields_dictionary(self):
        return {'nickname': self._nickname, 'limbs_count': self._limbs_count, 'is_bird': 0}

    def __str__(self):
        return 'Nickname = {0}, Limbs count = {1}' \
            .format(self._nickname, self._limbs_count)
