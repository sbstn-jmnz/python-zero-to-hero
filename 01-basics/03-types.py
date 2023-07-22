# Podemos pensar que en Python todo es un Valor, Valores que hemos visto son:
# "Hola Mundo", 2, 4, "Harvys". Todos los valores tienen un TIPO. Y depende del tipo las operaciones que podemos realizar con ellos

# Para ver el tipo de un valor, tenemos la función type()

print(type("Hola Mundo")) # Los textos son de tipo string o str
print(type(2)) # Los números enteros son de tipo int
print(type(3.2)) # Los números con parte decimal son float

phrase_one = "Hola Mundo"

# Le pasamos a print una operación con valores. Estamos "sumando" textos
print(phrase_one + " " + phrase_one)

# Le pasamos a print 2 veces el valor, separado por comas y automáticamente los separa con un espacio
print(phrase_one,phrase_one)

# Multiplicar texto
print(phrase_one * 3)

# Pero no podemos sumar textos con números

# print(phrase_one + 4)

# print(phrase_one/phrase_one)