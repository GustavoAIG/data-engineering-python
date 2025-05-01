# Ejercicio 2: Suma de 5 números
# Pide al usuario 5 números y calcula su suma total.

numeros = []
suma = 0

for i in range(5):
    num = int(input(f"{i +1 }. Ingrese un número: "))
    numeros.append(num)
    suma += num

print(f"La lista es: {numeros}")
print(f"La suma total es: {suma}")