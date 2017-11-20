class car:

    def __init__(self):
        self.gosnomer=""
        self.mark=""
        self.model=""
        self.horsepower=0
        self.mileage=0
        self.edit={"gosnomer":self.add_gosnomer,
                   "mark":self.add_mark,
                   "model":self.add_model,
                   "horsepower":self.add_horsepower,
                   "mileage":self.add_mileage}

    def add(self):
        self.add_gosnomer()
        self.add_mark()
        self.add_model()
        self.add_horsepower()
        self.add_mileage()

    def add_gosnomer(self):
        self.gosnomer=input("Enter gosnomer\n")

    def add_mark(self):
        self.mark=input("Enter mark\n")

    def add_model(self):
        self.model=input("Enter model\n")
        
    def add_horsepower(self):
        while(True):
            self.horsepower=input("Enter horsepower\n")
            if is_int(self.horsepower):
                break

    def add_mileage(self):
        while(True):
            self.mileage=input("Enter mileage\n")
            if is_float(self.mileage):
                break

    def show_car(self):
        print("""
gosnomer: {0}
mark: {1}
model: {2}
horsepower: {3}
mileage: {4}""".format(self.gosnomer,self.mark,self.model,self.horsepower,self.mileage))

    def edit_car(self):
        self.show_car()
        while(True):
            inp=input("\nEnter the parameter for editing. To return enter 'back'.\n")
            if (str(inp)=="back"):
                break
            else:
                try:
                    self.edit[str(inp)]()
                except:
                    inp=input("\nEnter the parameter for editing. To return enter 'back'.\n")
