# Portafolio Módulo 4 - Python

Sistema de gestión de biblioteca implementado en Python como evidencia de competencias técnicas en POO y manejo de archivos.

## 📋 Requerimientos Cumplidos

| Competencia          | Implementación                                                                 |
|----------------------|-------------------------------------------------------------------------------|
| Programación Orientada a Objetos | Clases `Libro`, `LibroDigital` y `Biblioteca` con herencia y encapsulamiento |
| Manejo de archivos   | Persistencia de datos en `biblioteca.txt`                                    |
| Validación de datos  | Setters con verificación de estados (`disponible`/`prestado`)                |
| Modularización       | Proyecto dividido en 4 archivos lógicos                                      |
| GitHub               | Repositorio con historial de commits progresivos                             |

## 📁 Estructura del Proyecto
```EV-PortafolioM4/
├── _1_libro.py # Clase base Libro (getters/setters)
├── _2_libro_digital.py # Clase hija LibroDigital (herencia)
├── _3_biblioteca.py # Gestión y persistencia de libros
├── _4_main.py # Menú interactivo
├── biblioteca.txt # Datos de prueba
└── README.md # Este archivo
```
## 🚀 Cómo Ejecutar
```bash
# Ejecutar el sistema completo:
python _4_main.py
```

## 📐 Diagrama de Clases

```mermaid
classDiagram
    class Libro {
        -_titulo: str
        -_autor: str
        -_año_publicacion: str
        -_estado: str
        +titulo: property
        +autor: property
        +año_publicacion: property
        +estado: property
        +__str__() str
    }

    class LibroDigital {
        -_formato: str
        +__str__() str
    }

    class Biblioteca {
        -_libros: list[Libro]
        +agregar_libro()
        +eliminar_libro()
        +listar_libros()
        +buscar_libro()
        +marcar_prestado()
        +devolver_libro()
        +cargar_libros()
        +guardar_libros()
    }

    Libro <|-- LibroDigital : Herencia
    Biblioteca "1" *-- "0..*" Libro : Contiene
