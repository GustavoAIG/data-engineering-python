# Ejercicio 3: Par o impar
# Escribe un programa que diga si un número ingresado por el usuario es par o impar.

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")