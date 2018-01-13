class Computer_case:
        
    def read(self):
        print("Enter the computer name")
        self.name = input()
        print("Enter motherboard")
        self.motherboard = input()
        print("Enter CPU")
        self.CPU = input()
        print("Enter HDD")
        self.HDD = input()
        print("Enter RAM")
        self.RAM = input()
        print("Enter GPU")
        self.GPU = input() 
        
    def write(self):
        l=[["name", self.name], ["motherboard", self.motherboard], ["CPU", self.CPU], ["HDD", self.HDD], ["RAM", self.RAM], ["GPU", self.GPU]]
        return l
