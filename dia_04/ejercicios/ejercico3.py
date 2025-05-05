# Ejercicio 3: Promedio de notas
# Pide al usuario las notas de 5 cursos, calcula y muestra el promedio.

notas = []
suma = 0
for i in range(5):
    nota = int(input(f"{i+1}. Ingresa la nota del curso: "))
    notas.append(nota)
    suma += nota

promedio = suma / 5
print(f"El promedio de las notas de 5 cursos es: {promedio}")