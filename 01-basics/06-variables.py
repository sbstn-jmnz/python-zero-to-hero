# Vimos que a los valores se les puede asignar un nombre. Este nombre se conoce como variable.  
# Tal como su nombre lo indica, podemos utilizar el mismo nombre para apuntar a diferentes valores, uno a la vez

# Cuando primero le damos el valor a una variable lo llamamos ASIGNACIÓN
name = "sebastian"

print(name.title())

# Cuando reutilizamos la variable con un nuevo valor se llama RE ASIGNACIÓN 
name = "sebastián jiménez"

print(name.title())

# Los nombres de las variables son sensibles a las mayúsculas y minúsculas:

NAME = "Soy Más"
Name = "Python"

print(name,NAME,Name)

# Los nombres de las variables no pueden partir con un número y tampoco pueden coincidir con las palabras reservadas de python
# https://flexiple.com/python/python-reserved-words/

# Para variables de más de una palabra utilizar el _ 
cake_type = "Napolitana" 