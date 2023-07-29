# Escribir un programa que imprima una lista de los estudiantes con promedio superior a 6

averages = {
  "Seba": 5,
  "Gaby": 6.5,
  "Fran": 7,
  "Jose": 6.4,
  "Coni": 6.2,
  "Gonza": 4.8
}

# 1 Crear una lista vacía
approved = []
# 2 recorrer las llaves del diccionario
for key in averages.keys():
# 3 revisar si el valor de la llave es superior a 6
  if averages[key] > 6:
# 4 agregar la llave a lista
    approved.append(key)
# 5 Imprimir la lista
print(approved)