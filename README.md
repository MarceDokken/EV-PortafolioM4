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
