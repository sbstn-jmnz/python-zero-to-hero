# Calcular con ayuda de un for la suma de todos los elementos de la siguiente lista
numbers = [14,52,54,64,76,23,5,2,54,6,32]
# La variable result actúa como un acumulador
result = 0
for num in numbers:
  result += num

print(result)

print(sum(numbers))