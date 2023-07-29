# Las funciones pueden definir en su cuerpo variables, pero estas variables son parte de su alcance, o ámbito y no son accesibles desde fuera de la función.

def say_hello(name, lastname):
  fullname = name + " " + lastname
  print("Hola", fullname)

say_hello("Seba", "Jmnz")

fullname
