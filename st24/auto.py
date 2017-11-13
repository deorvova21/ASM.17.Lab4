class Auto:
    def __str__(self):
        out = ('Название: ' + self.name
               + '\nГод выпуска: ' + self.year
               + '\nЦвет: ' + self.color)
        return out

    def edit(self):
        self.name = input('Название: ')
        self.year = input('Возраст: ')
        self.color = input('Год выпуска: ')
        return {'name':self.name, 'year': self.year, 'color': self.color}
