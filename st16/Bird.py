from .Animal import Animal


class Bird(Animal):
    __beak_length: int = 0

    def __init__(self, name, limbs_count, beak_length):
        super().__init__(name, limbs_count)
        self.__beak_length = beak_length

    def get_fields_dictionary(self):
        tmp = super().get_fields_dictionary()
        tmp.update({'is_bird': 1})
        tmp.update({'beak_length': self.__beak_length})
        return tmp

    def __str__(self):
        return 'Nickname = {0}, Limbs count = {1}, Beak length = {2}'\
            .format(self._nickname, self._limbs_count, self.__beak_length)
