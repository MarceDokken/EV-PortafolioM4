import os

class Biblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self._libros = []  # Lista de libros
        self._archivo = archivo  # Archivo para persistencia
       
       #Estructuca base de Biblioteca