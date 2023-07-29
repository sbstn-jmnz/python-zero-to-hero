# Los diccionarios son similares a las listas, pero en lugar de índices, podemos tener cualquier otro valor que se único en el diccionario

# Ejemplo:
# curly braces
empty_list = {}

# Los elementos en un diccionario van en pares, es decir, llevan su llave y su valor
english_to_spanish = {"hi":"hola", "bye": "chao"}

# A diferencia de las listas, los diccionarios obtienen los valores mediante la llave

print(english_to_spanish["hi"])
print(english_to_spanish["bye"])

# Podemos decir que la posición de los valores no es tan relevante como lo es en las listas

print(english_to_spanish)

# Los diccionarios también son colecciones. Por lo tanto tienen un largo con la cantidad de elementos
print(len(english_to_spanish))

