# Con lo que hemos aprendido hasta ahora, es posible hacer cualquier programa imaginable. Es decir, utilizando solamente las estructuras de control, los loops, y variables, en teoría podríamos hacer cualquier programa. Si solo lo hacemos con estas partes básicas tendremos muchas líneas de código y una complejidad imposible de manejar. 

# Por eso existen otras formas de ORGANIZAR el código del programa para que sea más fácil de entender y actualizar por parte de los desarrolladores. Una de estas formas de organizar el código son las funciones.  "Spageti code"



dog = ["Benito", 2, "labrador"]
dog2 = ["Fito Andrés", 2, "híbrido"]

print(f"{dog[0]}")
# Hola soy Benito, un labrador, de 2 años
class Dog:
  def __init__(self,name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed 
    
  def say_hello(self):
    return f"Hola soy {self.name}, un {self.breed}, de {self.age} años"


beni = Dog("Benito", 2, "labrador")
fito = Dog("Fito Andrés",2,"híbrido")

print(beni.say_hello())
print(fito.say_hello())