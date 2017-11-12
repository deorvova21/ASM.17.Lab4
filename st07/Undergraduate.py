from .Student import *

class Undergraduate(Student):
    def __str__(self):
        return 'Старшекурсник:\n Имя: %s\n Возраст: %s\n Курс: %s\n Тип: %s\n Научный руководитель: %s\n Тема диплома: %s\n' %(self.name, self.age, self.year, self.payment, self.advisor, self.topic)

    def Edit(self):
        result = super().Edit()
        self.advisor = input('Научный руководитель: ')
        self.topic = input('Тема диплома: ')
        result['advisor'] = self.advisor
        result['topic'] = self.topic
        return result
        
