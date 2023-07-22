# Hacer un programa de determine el perímetro de una torta en centímetros
# Nota para el valor de pi, utilizar 3.14
# El usuario del programa ingresará mediante el teclado el radio de la torta.

cake_radius = int(input("Indicar el radio de la torta en centímetros: "))

# Perímetro de una circunferencia
# 3.14 * diámetro
# 3.14 * 2 * radio

perimeter = 2 * 3.14 * cake_radius

print("El perímetro de la torta es", perimeter, "centímetros")
