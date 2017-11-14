class Candidate:

    def read(self):
        print("Введите имя:")
        self.first_name = input()
        print("Введите фамилию:")
        self.last_name = input()
        print("Введите пол:")
        self.gender = input()
        print("Введите возраст:")
        self.age = input()
        print("Введите E-mail:")
        self.mail = input()

    def write(self):
        l=[["first_name", self.first_name], ["last_name", self.last_name], ["gender", self.gender], ["age", self.age], ["mail", self.mail]]
        return l
