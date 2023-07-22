# Una evaluación condicional puede estar dentro de otra:

name = input("Hola, cuál es tu nombre? ")
age = int(input("Dime tu edad "))

if age >= 18:
  drink = input("¿Quieres cerveza o vino?")
  print("Toma",name)
  if drink == "cerveza":
    print("Aquí tienes tu cerveza")
  else:
    print("Aquí está tu vino")
else:
  juice = input("¿Quieres jugo de frutilla o naranja?")
  print("Toma", name)
  if juice == "frutilla":
    print("Acá está tu jugo de frutilla")
  else:
    print("aquí tienes tu jugo de naranjas")