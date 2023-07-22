# Hacer un programa que imprima lo siguiente utilizando for, if print y variables

# 1 3 5 7 9
#  2 4 6 8

odds = ""
even = ""
for num in range(1,10):
  if num % 2 == 0:
    # str() es como en inverso de int(), es decir, transforma un número en un string
    even += str(num)
    odds += " "
  else:
    odds += str(num)
    even += " "

print(odds)
print(even)
