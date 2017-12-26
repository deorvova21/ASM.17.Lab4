import cgi
from .Car import *

class Driver(Car):
    def __init__(self, dname='',lastname=''):
        super().__init__()
        self.dname=dname
        self.lastname=lastname
        
    def write(self):
        driver={'name':self.name, 'color':self.color, 'price':self.price, 'dname':self.dname, 'lastname':self.lastname}
        return driver
    
    def edit(self):
        self.name=input('Name: ')
        self.color=input('Color: ')
        self.price=input('Price: ')
        self.dname=input('Dname: ')
        self.lastname=input('Lastname: ')
        
