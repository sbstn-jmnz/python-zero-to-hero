# Crear una función que retorne la suma de todos los números hasta el número number pasado como parámetro

# sum_up(5) # => 1+2+3+4+5 = 15

def sum_up(number):
  result = 0
  for num in range(number + 1):
    result = result + num  
  return result


print(sum_up(5))
print(sum_up(4))
print(sum_up(6))


