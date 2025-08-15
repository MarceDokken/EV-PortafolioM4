from _1_libro import Libro
import os

class Biblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self._libros = []
        self._archivo = archivo
        self._cargar_libros()  

    def _cargar_libros(self):
        """Carga los libros desde el archivo al iniciar."""
        if os.path.exists(self._archivo):
            with open(self._archivo, 'r') as f:
                for linea in f:
                    datos = linea.strip().split('|')
                    if len(datos) == 4:
                        self._libros.append(
                            Libro(datos[0], datos[1], int(datos[2]), datos[3])
                        )

    def _guardar_libros(self):
        """Guarda todos los libros en el archivo."""
        with open(self._archivo, 'w') as f:
            for libro in self._libros:
                f.write(f"{libro.titulo}|{libro.autor}|{libro.anio}|{libro.estado}\n")

    def agregar_libro(self, libro: Libro) -> bool:
        """Añade un libro si no existe otro con el mismo título (insensible a mayúsculas)."""
        if not any(l.titulo.lower() == libro.titulo.lower() for l in self._libros):
            self._libros.append(libro)
            self._guardar_libros()  
            return True
        return False

    def listar_libros(self) -> list[Libro]:
        """Devuelve una copia de la lista de libros."""
        return self._libros.copy()

    def buscar_libro(self, titulo: str) -> Libro | None:
        """Busca un libro por título (insensible a mayúsculas)."""
        for libro in self._libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo: str) -> bool:
        """Marca un libro como 'prestado' si está disponible."""
        libro = self.buscar_libro(titulo)
        if libro and libro.estado == "disponible":
            libro.estado = "prestado"
            self._guardar_libros()
            return True
        return False

    def devolver_libro(self, titulo: str) -> bool:
        """Marca un libro como 'disponible' si estaba prestado."""
        libro = self.buscar_libro(titulo)
        if libro and libro.estado == "prestado":
            libro.estado = "disponible"
            self._guardar_libros()
            return True
        return False