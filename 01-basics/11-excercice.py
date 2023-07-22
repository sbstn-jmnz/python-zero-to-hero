# Crear un programa que pida el radio de una torta en centímetros y diga si la torta es para 15, 25 o 30 personas

cake_radius = int(input("Indicar el radio de la torta en centímetros: "))

  # Si el radio está entre 10 y 15 es para 15 personas 
if(cake_radius > 10 and cake_radius <= 15):
  print("Torta para 15 personas")

# Si el radio está entre 16 y 25 es para 25 personas
elif(cake_radius > 16 and cake_radius <= 25):
  print("Torta para 25 personas")

# y si es mayor a 25 es para 30
elif cake_radius > 25:  
  print("Torta para 30 personas")

# Si es menor a 10 es individual 
elif cake_radius < 10: 
  print("Torta individual")
