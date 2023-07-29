# Crear una función que reciba como parámetro una lista de números e imprima su promedio

def print_average(nums_list):
  print(sum(nums_list)/len(nums_list))


print_average([1,2,3,4,5,6,7,5,34,23])
print_average([1,2,3])

# Crear una función que reciba como parámetro una lista de números y retorne una NUEVA lista de los números impares

def odd_numbers(nums_list):
  odds = []
  for num in nums_list: 
    if num % 2 == 1:
      odds.append(num)
  return odds

result_one = odd_numbers([1,2,3,4,5,6,7,5,34,23])
result_two = odd_numbers([1,2,3])

print(result_one)
print(result_two)