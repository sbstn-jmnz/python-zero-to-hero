# Con append podemos agrega más información al archivo

dataFile = open("./sample_two.txt", "a")

for i in range(1,4):
  dataFile.write(f"A la {i} \n")

dataFile.close()