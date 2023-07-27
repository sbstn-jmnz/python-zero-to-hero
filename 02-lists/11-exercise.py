# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

user_number = int(input("Ingresa el número de palabras para la lista "))
words = []

for number in range(user_number):
  word = input(f"Ingresa la palabra {number +1}: ")
  words.append(word)

search = input("Ingresa la palabra a buscar: ")
counter = 0
if search in words:
  for word in words:
    if search == word:
      counter += 1
  if counter == 1:
    print("La palabra está", counter, "vez")
  else:
    print("La palabra está", counter, "veces")
else:
  print("La palabra no está en la lista")
