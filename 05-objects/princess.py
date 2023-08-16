class Princess:
  def __init__(self,name, age):
    self.name = name
    self.age = age
    self.life = 10

  def ending(self):
    return f"Soy {self.name} y conquisté el reino a mis {self.age}"

  def fight(self, enemy):
    enemy.life -= 1 

def main():
  print("Módulo de princesas")
  
  jazmin = Princess("Jazmine", 20) 
  print(jazmin.ending())
  
  mulan = Princess("Mulán", 21)
  print(mulan.ending())
  
  print(Princess("Cenicienta", 24).ending())

if __name__ == "__main__":
  main()
  