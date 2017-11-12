class Client:
    def __init__(self):
        self.setName(input("Введите имя клиента >>  "))
        self.setGender(input("Введите пол клиента >>  "))        
        self.setAge(input("Введите возраст клиента >>  "))
        self.setWeight(input("Введите вес клиента >>  "))
        self.setPhone(input("Введите телефон клиента >>  "))
    def edit(self):
        self.setName(input("Введите имя клиента >>  "))
        self.setGender(input("Введите пол клиента >>  ")) 
        self.setAge(input("Введите возраст клиента >>  "))
        self.setWeight(input("Введите вес клиента >>  "))
        self.setPhone(input("Введите телефон клиента >>  "))
    def setName(self, inputValue):
        self.name = inputValue
    def setGender(self, inputValue):
        self.gender = inputValue
    def setAge(self, inputValue):
        self.age = inputValue
    def setWeight(self, inputValue):
        self.weight = inputValue
    def setPhone(self, inputValue):
        self.phone = inputValue
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getAge(self):
        return self.age
    def getWeight(self):
        return self.weight
    def getPhone(self):
        return self.phone
    def __str__(self):
        self.string = 'Клиент: ' + self.getName() + ' Возраст: ' + str(self.getAge()) + ' Вес: ' + str(self.getWeight()) + ' Телефон: ' + self.getPhone()
        return self.string