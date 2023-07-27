for row  in range(10):
  line = ""
  for col in range(10):
    if col == row or col + row == 9:
      line += "*"
    else:
      line += " "
  print(line)