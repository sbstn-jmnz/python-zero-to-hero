# Para escribir utilizamos el modo w con la función open

data = open('sample_two.txt', 'w')

for i in range(4):
  data.write(f"Hola pescao {i} \n")

print(data.read())

data.close()
