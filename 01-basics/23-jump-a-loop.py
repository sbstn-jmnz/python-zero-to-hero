# Podemos saltar una iteración o vuelta usando la palabra clave continue

spaces = ""
for letter in "murciélago":
  if letter == "l":
    continue
  spaces += " "
  print(spaces,letter)
  