from st20.car import car 

class truck(car):

    def __init__(self):
        car.__init__(self)
        self.height=0
        self.carrying=0
        self.edit["height"]=self.add_height
        self.edit["carrying"]=self.add_carrying

    def add(self):
        car.add(self)
        self.add_height()
        self.add_carrying()

    def add_height(self):
        while(True):
            self.height=input("Enter height\n")
            if is_float(self.height):
                break

    def add_carrying(self):
        while(True):
            self.carrying=input("Enter carrying\n")
            if is_float(self.carrying):
                break

    def show_car(self):
        car.show_car(self)
        print("""height: {0}
carrying: {1}""".format(self.height,self.carrying))
