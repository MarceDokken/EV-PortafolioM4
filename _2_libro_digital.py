from _1_libro import Libro

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, estado="disponible"):
        super().__init__(titulo, autor, anio, estado)
        self._formato = formato  

    def __str__(self):
        return f"[Digital] {super().__str__()} | Formato: {self._formato}"