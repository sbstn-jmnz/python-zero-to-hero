# La ejecución condicional de código se realiza evaluando sentencias lógicas. Estas sentencias entregan un valor de tipo Booleano (Bool), es decir entregan True o False
# 
print("-------Expresiones Booleanas")
print(5 > 4)
print(5 < 4)
print(4 == 4)
print(4 == '4')
print(4 != 4)

# Si queremos comparar menor o igual
print(4 <= 4)
# Para mayor o igual
print(4 >= 4)

# Podemos también tener expresiones booleanas compuestas utilizando los operadores and, or y not
print("----------------Expresiones Booleanas Compuestas------------")
print(4 < 5 or 6 > 8) # True or False => True
print(4 < 5 and 6 > 8) # True and False => False
print(4 > 5 and 6 > 8) # False and False => False

print(not True)
print(not False)