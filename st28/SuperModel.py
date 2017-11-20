from .Model import *


class SuperModel(Model):
    magazine = 'None'

    def get_params(self):
        return {'surname': self.surname,'name': self.name, 'age': self.age, 'growth': self.growth,
                'weight': self.weight, 'magazine': self.magazine, 'is_supermodel': 1}