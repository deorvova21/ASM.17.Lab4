class Model:
    surname = 'None'
    name = 'None'
    age = 0
    growth = 0
    weight = 0

    def get_params(self):
        return {'surname': self.surname,'name': self.name, 'age': self.age,
                'growth': self.growth,'weight': self.weight, 'is_supermodel': 0}

    def __str__(self):
        return self.name
