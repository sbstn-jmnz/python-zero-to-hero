# El for es una estructura que sirve para ejecutar un conjunto de sentencias por cada elemento de una colección. Además el for no da una variable para acceder en cada vuelta al elemento que corresponde.

banana = "Esto es un ejemplo"

# Esta es la forma manual carretera, ordinaria, picante, vulgar
print(banana[0])
print(banana[1])
print(banana[2])
print(banana[3])
print(banana[4])
print(banana[5])
print(banana[6])

print("-----------------------------")
# Esta es la forma pirula, elegante o correcta de recorrer el texto usando un while
index = 0
while index < len(banana):
  print(banana[index])
  index += 1

print("-----------------------------")

# Esta la forma más sencilla, elegante o pythonezca de recorrer un string
for element in banana:
  print(element)





