from _3_biblioteca import Biblioteca
from _1_libro import Libro

def mostrar_menu():
    print("\n=== GESTOR DE BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Salir")

def main():
    biblioteca = Biblioteca()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            try:
                print("\n--- AGREGAR LIBRO ---")
                titulo = input("Título: ")
                autor = input("Autor: ")
                anio = int(input("Año: "))
                libro = Libro(titulo, autor, anio)
                
                if biblioteca.agregar_libro(libro):
                    print(f"✓ Libro '{titulo}' agregado!")
                else:
                    print(f"✗ Error: El libro ya existe.")
            
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            libros = biblioteca.listar_libros()
            print("\n--- LISTA DE LIBROS ---")
            if libros:
                for libro in libros:
                    print(libro)
            else:
                print("No hay libros registrados.")

        elif opcion == "3":
            titulo = input("\nTítulo a buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            print("--- RESULTADO ---")
            print(libro if libro else "✗ Libro no encontrado")

        elif opcion == "4":
            titulo = input("\nTítulo a prestar: ")
            if biblioteca.prestar_libro(titulo):
                print(f"✓ Libro '{titulo}' prestado!")
            else:
                print(f"✗ Error: No disponible o no existe")

        elif opcion == "5":
            titulo = input("\nTítulo a devolver: ")
            if biblioteca.devolver_libro(titulo):
                print(f"✓ Libro '{titulo}' devuelto!")
            else:
                print(f"✗ Error: No estaba prestado o no existe")

        elif opcion == "6":
            print("\n¡Gracias por usar el sistema!")
            break

        else:
            print("\n✗ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()