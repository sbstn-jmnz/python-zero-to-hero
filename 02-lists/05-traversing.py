# La forma más frecuente de recorrer una lists es utilizando el loop for

activities = ["sleep", "eat", "study"]

# utilizamos el for para recorrer directamente en la lista
for activity in activities:
  print(activity.title())

# Atención
# Lo anterior funciona bien si queremos utilizar directamente los valores existentes, pero si queremos actualizar algún valor, necesitaremos los índices
print("---------------------------")
# Utilizamos el for sobre un rango desde cero hasta la ultima posición de la lista. En todo momento es un rango de NÚMEROS
# Podemos utilizar esos números como índices para acceder a los elementos de la lista.
for position in range(len(activities)):
  activities[position] = "sleep" 

print("---------------------------")
print(activities)


cities = ["bogotá", "caracas","lima","la paz","san josé"]

for city in cities:
  print(city.title())

for position in range(len(cities)):
  cities[position] = cities[position].title()

print(cities)

# ["Bogotá", "Caracas","Lima", "La Paz", "San José"]

numbers = [4,3,5,6,7,4,3,5,6,7]

for n in range(len(numbers)):
  numbers[n] = numbers[n] * 2

print(numbers)


# [8,6,10,12,14,8,6,10,12,14]