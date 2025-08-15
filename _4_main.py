from _3_biblioteca import Biblioteca

def mostrar_menu():
    print("\n=== MENÚ BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Salir")

def main():
    biblioteca = Biblioteca()
    while True:
        mostrar_menu()
        opcion = input("Opción: ")
        if opcion == "3":
            print("¡Hasta luego!")
            break
        print("Función en desarrollo...")

if __name__ == "__main__":
    main()