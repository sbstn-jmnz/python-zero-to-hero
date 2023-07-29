# Recorrer el diccionario e imprimir cada estudiantes de la siguiente forma

# El estudiante x reprobó con promedio y
# El estudiante X aprobó con promedio x

# La nota de aprobación la debe ingresar el usuario

averages = {
  "Seba": 5,
  "Gaby": 6.5,
  "Fran": 7,
  "Jose": 6.4,
  "Coni": 6.2,
  "Gonza": 4.8
}

# 1 Recorrer las llaves del diccionario
for key in averages.keys():
# 2 revisar si el valor es mayor a 6
  if averages[key] > 6:
  # Imprimir los aprobados
    print("El estudiante", key ,"aprobó con promedio", averages[key])
  else:
  # Imprimir los reprobados
    print("El estudiante", key ,"reprobó con promedio", averages[key])

