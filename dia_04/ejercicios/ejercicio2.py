# Ejercicio 2: Números al cuadrado
# Pide al usuario 5 números, guárdalos en una lista, y crea otra lista con sus cuadrados.

numeros = []
cuadrados = []
for i in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

for i in numeros:
    cuadrados.append(i * i)

for i in cuadrados:
    print(i)
