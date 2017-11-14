from .Run import Run

class Marathon(Run):
    attrs = ('length', 'time', 'date', 'place')
    names = ('Дистанция (в км)', 'Время (в мин)', 'Дата', 'Место')
    
    def __init__(self, number=-1, length=0, time=0, date='', place=1):
        Run.__init__(self, number, length, time, date)
        self.place = place