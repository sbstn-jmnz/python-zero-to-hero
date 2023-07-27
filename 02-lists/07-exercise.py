# Calcular con ayuda de un for el promedio de todos los elementos de la siguiente lista
numbers = [14,52,54,64,76,23,5,2,54,6,32]
result = 0
for num in numbers:
  result = result + num

print(result/len(numbers))

print(sum(numbers)/len(numbers))