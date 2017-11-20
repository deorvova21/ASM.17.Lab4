class Dish:

    def __init__(self):
        self.name=""
        self.price=0
        self.grams=0
        self.description=""
        self.edit=[self.AddName,self.AddPrice,self.AddGrams,self.AddDescription]
    
    def AddDish(self):
        self.AddName()
        self.AddPrice()
        self.AddGrams()
        self.AddDescription()

    def AddName(self):
        self.name=input("Enter name\n")
    
    def AddPrice(self):
        self.price=WhileTest(IsFloat,self.price,"Enter price\n")

    def AddGrams(self):
        self.grams=WhileTest(IsFloat,self.grams,"Enter grams\n")

    def AddDescription(self):
        self.description=input("Enter description\n")

    def ShowDish(self):
        print("""
0) name - {0}
1) price - {1}
2) grams - {2}
3) description - {3}""".format(self.name,self.price,self.grams,self.description))

    def EditDish(self):
        self.ShowDish()
        p=""
        while(True):
            i=WhileTest(IsInt,p,"\nEnter the parameter dish number for editing. To return enter -1.\n")
            if (int(i)==-1):
                break
            self.edit[int(i)]()
            self.ShowDish()
