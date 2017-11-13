from .Worker import *

class Fired(Worker):
    def __str__(self):
        return super().__str__() + 'Дата увольнения: {}\nПричина увольнения: {}'.format(self.date, self.reason)

    def Edit_Show(self):
        result = super().Edit_Show()
        self.date = input("Дата увольнения: ")
        self.reason = input("Причина увольнения: ")
        result['date'] = self.date
        result['reason'] = self.reason
        return result
        
