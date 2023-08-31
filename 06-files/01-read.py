# Leer un archivo con open()
data = open('./sample.txt','r')

# Leemos el contenido con el método read()
print(data.read())

# Importante cerrar el archivo
data.close()