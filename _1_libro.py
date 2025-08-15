class Libro:
    def __init__(self, titulo, autor, anio, estado="disponible"):
        self.titulo = titulo 
        self.autor = autor
        self.anio = anio
        self.estado = estado

    def __str__(self):
        return f"{self.titulo} ({self.anio}), por {self.autor} - {self.estado}"