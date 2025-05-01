# Desafío opcional del día
# Haz un validador de contraseña simple:
# La contraseña debe tener al menos 8 caracteres.
# Debe contener al menos una letra y un número.
# Muestra "Contraseña segura" o "Contraseña débil".

contrasenia = input("Ingrese su contraseña: ")

if len(contrasenia) < 8:
    print("Contraseña débil: debe tener al menos 8 caracteres.")
else:
    tiene_letra = False
    tiene_numero = False

    for caracter in contrasenia:
        if caracter.isalpha():
            tiene_letra = True
        elif caracter.isdigit():
            tiene_numero = True

    if tiene_letra and tiene_numero:
        print("Contraseña segura.")
    else:
        print("Contraseña débil: debe cotener letras y números.")