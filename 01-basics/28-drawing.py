for row in range(11):
  line = ""
  for col in range(11):
    if (col == row or col + row == 10):
      line += "*"
    elif row == 5 or col == 5:
      line += "*"
    else:
      line += " "
  print(line)

print("Hola gaby")


