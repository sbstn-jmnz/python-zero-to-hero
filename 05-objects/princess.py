class Princess:
  def __init__(self,name, age):
    self.name = name
    self.age = age
    self.life = 10

  def ending(self):
    return f"Soy {self.name} y conquisté el reino a mis {self.age}"

  def fight(self, enemy):
    enemy.life -= 1 

if __name__ == "__main__":

  jazmin = Princess("Jazmine", 20) 
  cenicienta = Princess("Cenicienta", 24)
  mulan = Princess("Mulán", 21)

  print(jazmin.ending())
  print(cenicienta.ending())
  print(mulan.ending())