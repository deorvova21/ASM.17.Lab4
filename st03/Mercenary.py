from .Soldier import Private

class Officer(Private):
    def __init__(self, name = '', surname = '', age = '', specialization = '', rank = '' , salary = ''):
        super(Officer, self).__init__(name , surname, age, specialization)
        self.rank = rank
        self.salary = salary

