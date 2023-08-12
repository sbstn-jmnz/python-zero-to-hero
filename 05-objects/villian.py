class Villian:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.life = 10
  
  def ending(self, princess):
    return f"Derroté a la princesa {princess.name} a sus {princess.age} años"
  
  def fight(self, princess):
    princess.life -= 1

if __name__ == "__main__":
  gru = Villian("Groot", 39)
  majin_buu = Villian("Majin Buu", 16)
  mojojojo = Villian("Mojojojo", 52)

