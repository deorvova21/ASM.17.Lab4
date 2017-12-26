import cgi

class Car:
    def __init__(self,name='',color='', price=''):
        self.name=''
        self.color=''
        self.price=''
        
    def write(self):
        car={'name':self.name, 'color':self.color, 'price':self.price}
        return car
    
    def edit(self):    
        self.name=input('Name: ')
        self.color=input('Color: ')
        self.price=input('Price: ')


    
    
