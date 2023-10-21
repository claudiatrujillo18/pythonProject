from Producto import Producto

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Registrar un producto")
        print("2. Imprimir la lista de productos")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == '1':
            Producto.registrar_producto()
        elif opcion == '2':
            Producto.imprimir_productos()
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Por favor, ingrese 1, 2 o 3.")


