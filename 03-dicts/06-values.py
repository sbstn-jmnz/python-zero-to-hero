# Podemos separar solo los valores de una diccionario utilizando su método .values()
english_to_spanish = {"one":"uno","two":"dos"}

values = english_to_spanish.values()

for val in values:
  print(val)