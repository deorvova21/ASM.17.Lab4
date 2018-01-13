from .computer_case import Computer_case

class Notebook(Computer_case):
    def __init__(self):
        super().__init__()
    
    def read(self):
        Computer_case.read(self)
        print("Enter the display")
        self.display = input()

    def write(self):
        l = Computer_case.write(self)
        l.append(["display", self.display])
        return l
    
    
