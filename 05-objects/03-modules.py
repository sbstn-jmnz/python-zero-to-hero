# Ya sabemos crear clases e instancias, es tiempo de pensar como organizarlos para programas más grandes. 
# Python nos permite usar módulos 

from princess import Princess
from villian import Villian
from random import choice
from time import sleep

print("Bienvenido al Juego de Princesas y Villanos")

while True:
  user_option = input("Escoge entre 1 para princesa o 2 villano, para salir ingresa 'q': ")
  
  if user_option == 'q' or user_option == 'Q':
    print("Gracias por participar")
    break

  elif user_option == "1":
    print("Muy bien, ya eres una princesa, ahora dime cuál")
    princess_name = input("Dime el nombre de la princesa: ")
    princess_age = input("Dime la edad de la princesa: ")
    
    user_princess = Princess(princess_name,princess_age)
    
    villians = ["Groot","Majin buu", "Mojojojo"]    
    villian = Villian(choice(villians), choice([39,16,54]))

    rounds = 0
    while user_princess.life > 1 or villian.life > 1:
      print("Round", rounds, "pelea")
      sleep(0.5)
      
      fight = choice([0,1])
      
      if fight == 1:
        user_princess.fight(villian)
        print("Atacó la princesa")
        print("Vida princesa", user_princess.life)
        print("Vida villano", villian.life)
      else:
        print("Atacó el villano")
        print("Vida princesa", user_princess.life)
        print("Vida villano", villian.life)
        villian.fight(user_princess)

      if villian.life == 0:
        print(user_princess.ending())
        break
      
      if user_princess.life == 0: 
        print(villian.ending(user_princess))
        break

      rounds += 1

  elif user_option == "2":
    print("Muy bien, ya eres un villano, ahora dime cuál")
    villian_name = input("Dime el nombre del villano")
    villian_age = input("Dime la edad del villano")


    princesses = ["Mulan", "Cenicienta", "Jazmín"]
    princess = Princess(choice(princesses), choice([20,24,21]))


    
  else:
    print("Ingresa una opción válida")

