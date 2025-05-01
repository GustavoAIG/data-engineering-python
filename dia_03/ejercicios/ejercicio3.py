# Ejercicio 3: Adivina el número
# Haz un juego donde el usuario intenta adivinar un número secreto del 1 al 10.
# Tiene hasta 3 intentos.

import random
numero = random.randint(1,10)


intentos = 3

while intentos > 0:
    n_ingresado = int(input("Intente adivinar el numero del 1 al 10: "))
    if n_ingresado == numero:
        print("¡Felicidades! Adivinaste el número.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"No es correcto. Intentos restantes: {intentos}")
        else:
            print(f"No adivinaste. El número correcto era {numero}.")