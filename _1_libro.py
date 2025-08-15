class Libro:
    def __init__(self, titulo: str, autor: str, anio: int, estado: str = "disponible"):
        self._titulo = titulo  
        self._autor = autor
        self._anio = anio
        self._estado = estado.lower()  

    # --- Getters ---
    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def autor(self) -> str:
        return self._autor

    @property
    def anio(self) -> int:
        return self._anio

    @property
    def estado(self) -> str:
        return self._estado

    # --- Setters ---
    @estado.setter
    def estado(self, nuevo_estado: str):
        """Valida que el estado sea 'disponible' o 'prestado'."""
        nuevo_estado = nuevo_estado.lower()
        if nuevo_estado in ("disponible", "prestado"):
            self._estado = nuevo_estado
        else:
            raise ValueError(f"Estado inválido: {nuevo_estado}. Use 'disponible' o 'prestado'.")

    # --- Representación legible ---
    def __str__(self) -> str:
        return f"{self._titulo} ({self._anio}), por {self._autor} | Estado: {self._estado}"