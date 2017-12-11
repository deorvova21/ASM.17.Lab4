from .Horses import Horses


class SportHorses(Horses):
 def __init__(self, id, name, age, color, type_of_sport):
        Horses.__init__(self, id, name, age, color)
        self.type_of_sport = type_of_sport
   
 def get_horse(self):
  return {
   'id': self.id,
   'name': self.name,
   'age': self.age,
   'color': self.color,
   'type_of_sport': self.type_of_sport
   }