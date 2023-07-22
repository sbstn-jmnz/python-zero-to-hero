import time
# Python los string ya son varios valores en uno. Cada string está compuesto de caracteres o letras.
some_text = "Algún texto de ejemplo"

# en un texto podemos acceder a cada letra utilizando los [] e indicando su posición partiendo desde 0
print(some_text[0]) # A
print(some_text[1]) # l
print(some_text[2]) # g

print("------------------------")

# En python los string son colecciones de caracteres. Veremos otras colecciones más adelante, como las listas y los diccionarios
# Las colecciones las podemos recorrer con el loop for que va a ejecutar su cuerpo una vez por cada elemento de la colección

index = 0
while(index < len(some_text)):
  print(some_text[index])
  index += 1

print("------------------------")

for letter in some_text:
  print(letter)






