from .auto import *

class Used(Auto):
    def __str__(self):
        super().__str__()
        out = ('\nКол-во владельцев: ' + self.owners
           + '\nПробег: ' + self.mileage)
        return out
    
    def edit(self):
        result = super().edit()
        self.owners = input('Кол-во владельцев: ')
        self.mileage = input('Пробег: ')
        result['owners'] = self.owners
        result['mileage'] = self.mileage
        return result
        
