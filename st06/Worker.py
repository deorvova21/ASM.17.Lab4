class Worker:
    def __str__(self):
        return '{}\nИмя: {}\nГод рождения: {}\nДолжность: {}\nОклад: {}\n'.format(self.type, self.name, self.year, self.position, self.salary)

    def Edit_Show(self):
        self.name = input("Имя: ")
        self.year = input("Год рождения: ")
        self.position = input("Должность: ")
        self.salary = input("Оклад: ")
        return {'name':self.name, 'year': self.year, 'position': self.position, 'salary': self.salary}
