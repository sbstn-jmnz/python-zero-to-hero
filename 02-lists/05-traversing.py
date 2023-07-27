# La forma más frecuente de recorrer una lists es utilizando el loop for

some_list = ["sleep", "eat", "study"]

for elem in some_list:
  print(elem.title())

# Lo anterior funciona bien si queremos utilizar directamente los valores existentes, pero si queremos actualizar algún valor, necesitaremos los índices
print("---------------------------")
for position in range(len(some_list)):
  some_list[position] = some_list[position].upper()

print(some_list)