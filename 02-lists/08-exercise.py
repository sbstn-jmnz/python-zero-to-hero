# Separar la lista en 2 listas, una con los números pares y otra con los impares y calcular su promedio 
numbers = [14,52,54,64,76,23,5,2,54,6,32]
even = []
odds = []

for num in numbers:
  # Si es par, el resto de la división por 2 es cero
  if num % 2 == 0:
    even.append(num)
  else:
    odds.append(num)

print("El promedio de los pares es:", sum(even)/len(even))
print("El promedio de los impares es:", sum(odds)/len(odds))

