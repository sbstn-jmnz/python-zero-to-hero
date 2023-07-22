# Prácticamente la totalidad de las aplicaciones y programas computacionales realizan las mismas operaciones:
# 1- TOMAR datos desde el exterior como el teclado, el mouse, las redes (internet) u algún otro dispositivo como sensores o cámaras.

# Python trae también una función básica para ingresar datos desde el teclado. La función input()

# 2- SALIDA de datos al exterior como la terminal, un archivo, enviarlo por la red (internet) o un parlante, etc

# Python trae para esto la función print() que veremos más en detalle después.

# 3- Otra operación que hace la mayoría de los programas es la EJECUCIÓN CONDICIONAL, que dependiendo de los valores ingresados, ejecuta el programa de cierta forma.
# Python trae para esto las ESTRUCTURAS DE CONTROL que también conoceremos más adelante.

# 4- También los programas realizan operaciones con los valores, ya sea combinando, sumando, acumulando, calculando, etc.

# 5- Repeticiones: Muchas veces para obtener un resultado es necesario repetir pasos sucesivos (receta de cocina) 


username = input("Hola. ¿Cuál es tu nombre?") 

print("Hola "+username)

if username == "Harvys":
  print("¡Somos tocayos!")

for letra in username:
  print(letra)



