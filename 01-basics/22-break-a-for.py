# Podemos terminar antes un loop utilizando la palabra clave break
# En general se utilizará con una estructura de control como el if/elif

spaces = ""
for letter in "murciélago":
  print(spaces,letter)

  if letter == "a":
    break
  
  spaces += " "