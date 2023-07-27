for row in range(10):
  line = ""
  for col in range(10):
    if row >= 0 and row < 6:
      if row == col or row + col == 9:
        line += "*"
      else:
        line += " "
    else:
      if row >= 6 and (col == 4 or col == 5):
        line += "*"
      else:
        line += " "
  print(line)