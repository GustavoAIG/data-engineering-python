# variables.py

# Variables personales
nombre = "TuNombre"
edad = 22
altura = 1.75
es_estudiante = True
lenguajes = ["Python","SQL", "Java"]

# Imprimir con formato
print(f"Hola, me llamo {nombre}, tengo {edad} años, mido {altura}m, y estoy aprendiendo {lenguajes}")

# Tipos de variables
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))
print(type(lenguajes))

# Desafío extra edad en días
edad_en_dias = edad * 365
print(f"Mi edad en días es aproximadamente {edad_en_dias} días.")