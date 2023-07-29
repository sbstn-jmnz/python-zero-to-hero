# Podemos tener diccionarios complejos con valores que también son colecciones

classroom = {
  "seba": {
    "name": "Sebastian Antonio",
    "age": 39,
    "grades": [6,5,4,6,5,4,5,6]
  },
  "gaby": {
    "name": "Gabriel Antonio",
    "age": 4,
    "grades": [7,6,5,6,7,7,6,5]
  },
  "gonza":{
    "name": "Gonzalo Ignacio",
    "age": 35,
    "grades": [5,6,4,5,6,7,6,5,4]
  }
}

print(len(classroom))
print(classroom.keys())