import datetime

class Run:    
    attrs = ('length', 'time', 'date')
    names = ('Дистанция (в км)', 'Время (в мин)', 'Дата')
    
    def __init__(self, number=-1, length=0, time=0, date=''):
        self.number = number
        self.length = length
        self.time = time
        
        if not date:
            now = datetime.datetime.now()
            self.date = '{0}.{1}.{2}'.format(str(now.day), str(now.month), str(now.year))
        else:
            self.date = date
        
    @property
    def type(self):
        return self.__class__.__name__
        
