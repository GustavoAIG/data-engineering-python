# Generador de tablas de multiplicar
# Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10.

numero = int(input("Ingrese un numero: "))

print(f"\nLa tabla de multiplicar de {numero} es: ")

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")