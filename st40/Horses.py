class Horses:
 def __init__(self, id, name, age, color):
  self.id = id
  self.name = name
  self.age = age
  self.color = color

 def get_horse(self):
  return {
   'id': self.id,
   'name': self.name,
   'age': self.age,
   'color': self.color
   }