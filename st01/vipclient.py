from .client import *
class Vipclient(Client):
    def __init__(self):
        Client.__init__(self)
        self.setParkingPlace(input("Введите парковочное место клиента >>  "))
        self.setPersonalTrener(input("Введите имя персонального тренера клиентаe >>  "))
    def edit(self):
        Client.edit(self)
        self.setParkingPlace(input("Введите парковочное место клиента >>  "))
        self.setPersonalTrener(input("Введите имя персонального тренера клиентаe >>  "))
    def setParkingPlace(self, inputValue):
        self.parking_place = inputValue
    def setPersonalTrener(self, inputValue):
        self.personal_trener = inputValue
    def getParkingPlace(self):
        return self.parking_place
    def getPersonalTrener(self):
        return self.personal_trener
    def __str__(self):
        Client.__str__(self)
        return 'Вип-'+self.string+ ' Парковочное место: ' + self.getParkingPlace() + ' Имя персонального тренера: ' + self.getPersonalTrener()