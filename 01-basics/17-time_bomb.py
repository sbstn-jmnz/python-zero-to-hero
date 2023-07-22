import time
# Hacer un programa que cuente regresivamente desde 10 y cuando al llegar a cero diga "Boom"

# 10
# 9
# 8
# ...
# Boom

num = 10
while (num >= 0):
  print(num)
  time.sleep(1)
  num = num - 1
print("Boom")