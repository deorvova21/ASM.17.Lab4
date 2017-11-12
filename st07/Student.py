class Student:
    def __str__(self):
        return 'Студент:\n Имя: %s\n Возраст: %s\n Курс: %s\n Тип: %s\n' %(self.name, self.age, self.year, self.payment)

    def Edit(self):
        self.name = input('Имя: ')
        self.age = input('Дата рождения: ')
        self.year = input('Группа: ')
        self.payment = input('Тип оплаты: ')
        return {'name':self.name, 'age': self.age, 'year': self.year, 'payment': self.payment}
