# Ejercicio 1: Edad y acceso
# Pide una edad y responde con un mensaje:
# Si es menor de 18: "Acceso denegado"
# Si es 18 o más: "Acceso permitido"

edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("Acceso denegado.")
else:
    print("Acceso permitido.")