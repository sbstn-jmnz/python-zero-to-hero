# Las funciones, no solo en python, si nó que en varios otros lenguajes, se pueden separar en 2 grande grupos. Las funciones que retornan o entregan un valor y las funciones que solamente ejecutan sentencias

def say_hello():
  print("hola")

def return_hello():
  return "hello"

say_hello()
print("--------------")
print(return_hello())

result_one = int(3.4)
result_two = print("Hola Mundo")

print(result_one)
print(result_two)

# Las funciones que retornan None, se le conoce como funciones vacías o void