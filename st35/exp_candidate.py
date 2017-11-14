from st35.candidate import Candidate

class Exp_Candidate(Candidate):

    def __init__(self):
        super().__init__()

    def read(self):
        Candidate.read()
        print("Введите опыт работы:")
        self.experience = input()
        print("Введите последнее место работы:")
        self.last_job = input()

    def write(self):
        l = Candidate.write(self)
        l.append(["experience", self.experience],["last_job", self.last_job])
        return l
