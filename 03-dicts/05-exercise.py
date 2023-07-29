search = input("¿Qué lenguaje quieres conocer? ")

lenguajes = {}

lenguajes["python"] = "Python is a programming language that lets you work more quickly and integrate your systems more effectively."
lenguajes["ruby"] = "Ruby is an interpreted, high-level, general-purpose programming language which supports multiple programming paradigms."
lenguajes["javascript"] = "JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies of the World Wide Web,"

# Crear un programa que muestre el valor de la llave solicitada si existe en el diccionario, y que diqa que no está si la llave no está en el diccionario 

if search in lenguajes:
  print("Sí está el lenguaje", search)
  print("Su valor es:", lenguajes[search])
else:
  print("No conozco el lenguaje", search )