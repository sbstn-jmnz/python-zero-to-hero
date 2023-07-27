for line in range(10):
  row = ""
  for col in range(10):
    if line % 2 == 0:
      if col % 2 == 0:
        row += " "
      else:
        row += "*"
    else:
      if col % 2 == 0:
        row += "*"
      else:
        row += " "
  print(row)

