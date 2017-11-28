from .food import *


class drink(food):
    
    def __init__(self):
        super().__init__()
        self.alcogol = ""
       


    def peredacha(self):
        inform = "&name="+urq.quote(self.name)+"&quantity="+urq.quote(self.quantity)+"&calories="+urq.quote(self.calories)+"&alcogol="+urq.quote(self.alcogol)
        return inform
