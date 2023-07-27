# Get: Obtener
# Para acceder a un elemento de la lista se usa el nombre de la variable seguido de [] indicando en su interior la posición del elemento partiendo desde cero.

fruits = ["pineapple", "banana", "orange"]

print(fruits[0])
print(fruits[-1])

# ATENCIÓN
# Podemos modificar un elemento de la lista de la siguiente forma
# Es decir, necesitamos utilizar el índice
fruits[1] = "chocolate"
# PRECAUCIÓN. Lo anterior borra el valor que había previamente

print(fruits)