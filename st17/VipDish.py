from st17.Dish import Dish

class VipDish(Dish):
    
    def __init__(self):
        Dish.__init__(self)
        self.bonus=0
        self.calories=0
        self.edit.append(self.AddBonus)
        self.edit.append(self.AddCalories)

    def AddVipDish(self):
        Dish.AddDish(self)
        self.AddBonus()
        self.AddCalories()

    def AddBonus(self):
        self.bonus=WhileTest(IsInt,self.bonus,"Enter bonus\n")

    def AddCalories(self):
        self.calories=WhileTest(IsFloat,self.calories,"Enter calories\n")

    def ShowDish(self):
        Dish.ShowDish(self)
        print("""4) bonus - {0}
5) calories - {1}""".format(self.bonus,self.calories))


