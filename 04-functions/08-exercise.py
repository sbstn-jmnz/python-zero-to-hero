# Hacer una función que imprima los números del 0 al number pasado como parámetro
# -------
# -- 0 --
# -- 1 --
# -- 2 --
# -- 3 --
# -- 4 --
# -- . --
# -- . --
# -- . --
# -- . --
# -- number --
# -------

def say_number(number):
  print("---------")
  for num in range(number+1):
    print("--",num,"--")
  print("---------")
  
say_number(5)

