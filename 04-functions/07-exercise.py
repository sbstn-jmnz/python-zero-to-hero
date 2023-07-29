# Crear una función que imprima cada elemento de la lista fruits
# de le siguiente forma 
# I like xxxxxxx

fruits_list = ["apple","orange","kiwi","banana"]
more_fruits = ["watermelon","mango","pineapple","pear"]

def print_fruits(fruits):
  for fruit in fruits:
    print("I like",fruit)

print_fruits(fruits_list)
print_fruits(more_fruits)