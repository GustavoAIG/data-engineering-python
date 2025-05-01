# Ejercicio 2: Clasificador de notas
# Dado un número del 0 al 20, muestra:
# 0-10 → "Desaprobado"
# 11-14 → "Aprobado"
# 15-18 → "Muy bien"
# 19-20 → "Excelente"

numero = int(input("Ingresa un numero del 0 al 20: "))

if numero < 0 or numero > 20:
    print("Número fuera de rango. Ingresa un valor entre 0 y 20.")
elif numero <= 10:
    print("Desaprobado")
elif numero <= 14:
    print("Aprobado")
elif numero <= 18:
    print("Muy bien")
else:
    print("Excelente")