# Utilizando 2 for podríamos representar filas y columnas como un papel milimetrado

size = int(input("¿De qué tamaño quieres el cuadrante?"))

for row in range(size + 1):
  line = ""
  for col in range(size + 1):
    line += f"({row},{col})"
  print(line)