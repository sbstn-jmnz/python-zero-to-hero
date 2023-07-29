# Crear un programa que haga un diccionario del largo que diga el usuario. Luego agregar el número de items que dijo el usuario con llave y valor. Pueden ser cualquier cosa.

dict_len = int(input("De qué largo quieres el diccionario: "))
dictionary = {}
for num in range(dict_len):
  key = input("Ingresa la llave: ")
  value = input("Ingresa el valor: ")
  dictionary[key] = value

print(dictionary)

