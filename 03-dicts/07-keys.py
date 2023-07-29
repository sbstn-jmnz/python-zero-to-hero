# Podemos separar solo las llaves de una diccionario utilizando su método .keys()
english_to_spanish = {"one":"uno","two":"dos"}

keys = english_to_spanish.keys()

for key in keys:
  print(key)