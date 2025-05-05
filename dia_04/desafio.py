# Gestor de lista de compras
# Permite al usuario:
# Agregar productos a una lista.
# Ver todos los productos agregados.
# Eliminar un producto por su nombre.
# Usa un bucle para que el menú se repita hasta que el usuario escriba "salir".

lista = []

while True:
    print("\n--- GESTOR DE LISTA DE COMPRAS ---")
    print("1. Agregar productos a una lista.")
    print("2. Ver todos los productos agregados.")
    print("3. Eliminar un producto por su nombre.")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto a agregar: ")
        lista.append(producto)
        print(f"{producto} agregado a la lista.")

    elif opcion == "2":
        if not lista:
            print("La lista está vacía.")
        else:
            print("Lista de productos:")
            for i, item in enumerate(lista, start=1):
                print(f"{i}. {item}")
    elif opcion == "3":
        producto = input("Ingrese el nombre del producto a eliminar: ")
        if producto in lista:
            lista.remove(producto)
            print(f" {producto} eliminado de la lista.")
        else:
            print(f"Producto no encontrado")

    elif opcion == "4":
        print("Saliendo del gestor de compras...")
        break

    else:
        print(f"Opción inválida. Intenta de nuevo")