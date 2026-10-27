import re

from autores_db import (
    obtener_autores_db, obtener_autor_db, insertar_autor_db
)
from libro_db import (
    obtener_libros_db, obtener_libro_db,
    insertar_libro_db, actualizar_libro_db, eliminar_libro_db
)

def mostrar_menu():
    print("\n==================================")
    print("   SISTEMA DE GESTIÓN - BIBLIOTECA")
    print("==================================")
    print("1. Listar todos los autores")
    print("2. Buscar autor por ID")
    print("3. Registrar nuevo autor")
    print("4. Listar todos los libros")
    print("5. Buscar libro por ID")
    print("6. Registrar nuevo libro")
    print("7. Actualizar un libro")
    print("8. Eliminar un libro")
    print("0. Salir")

def ejecutar_sistema():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccioná una opción: ")

        if opcion == '1':
            autores = obtener_autores_db()
            print("\n--- LISTA DE AUTORES ---")
            for a in autores:
                print(f"ID: {a['id']} | Nombre: {a['nombre']} | Nacionalidad: {a['nacionalidad']}")

        elif opcion == '2':
            id_autor = int(input("Ingresá el ID del autor: "))
            autor = obtener_autor_db(id_autor)
            if autor:
                print(f"\nEncontrado -> ID: {autor['id']} | Nombre: {autor['nombre']} | Nacionalidad: {autor['nacionalidad']}")
            else:
                print("\nAutor no encontrado.")

        elif opcion == '3':
            while True:
                nombre = input("Nombre del autor: ").strip()
                # Validar que solo tenga letras, espacios y vocales con tilde / ñ
                if re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre):
                    break
                print("❌ Error: El nombre solo debe contener letras y espacios. No se permiten símbolos.")

            while True:
                nacionalidad = input("Nacionalidad del autor: ").strip()
                if re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nacionalidad):
                    break
                print("❌ Error: La nacionalidad solo debe contener letras.")

            nuevo_id = insertar_autor_db(nombre, nacionalidad)
            print(f"\n¡Autor registrado con éxito! ID asignado: {nuevo_id}")

        elif opcion == '4':
            libros = obtener_libros_db()
            print("\n--- LISTA DE LIBROS ---")
            for l in libros:
                # Usamos 'anio' que es como viene de la base de datos
                print(f"ID: {l['id']} | Título: {l['titulo']} | Año: {l['anio']} | Autor ID: {l['autor_id']}")

        elif opcion == '5':
            id_libro = int(input("Ingresá el ID del libro: "))
            libro = obtener_libro_db(id_libro)
            if libro:
                print(f"\nEncontrado -> ID: {libro['id']} | Título: {libro['titulo']} | Año: {libro['anio']} | Autor ID: {libro['autor_id']}")
            else:
                print("\nLibro no encontrado.")
        elif opcion == '6':
            while True:
                titulo = input("Título del libro: ").strip()
                # Permite letras, números, espacios, tildes, ñ y puntuación básica
                if re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\.,:;'-]+$", titulo):
                    break
                print("❌ Error: El título contiene símbolos inválidos.")
            
            while True:
                try:
                    año = int(input("Año del libro: "))
                    break
                except ValueError:
                    print("❌ Error: Ingresá un año válido utilizando solo números.")
            
            while True:
                try:
                    autor_id = int(input("ID del autor asociado: "))
                    break
                except ValueError:
                    print("❌ Error: El ID del autor debe ser un número entero.")

            nuevo_id = insertar_libro_db(titulo, año, autor_id)
            print(f"\n¡Libro registrado con éxito! ID asignado: {nuevo_id}")

        elif opcion == '7':
            id_libro = int(input("ID del libro a actualizar: "))
            existente = obtener_libro_db(id_libro)
            if existente:
                print(f"Dejando en blanco o prescribiendo valores actuales: {existente['titulo']} ({existente['año']})")
                titulo = input(f"Nuevo título [{existente['titulo']}]: ") or existente['titulo']
                año_input = input(f"Nuevo año [{existente['año']}]: ")
                año = int(año_input) if año_input else existente['año']
                autor_id_input = input(f"Nuevo Autor ID [{existente['autor_id']}]: ")
                autor_id = int(autor_id_input) if autor_id_input else existente['autor_id']

                actualizar_libro_db(id_libro, titulo, año, autor_id)
                print("\n¡Libro actualizado correctamente!")
            else:
                print("\nLibro no encontrado.")

        elif opcion == '8':
            while True:
                try:
                    id_libro = int(input("ID del libro a eliminar: "))
                    break
                except ValueError:
                    print("❌ Error: El ID debe ser un número entero válido.")

            existente = obtener_libro_db(id_libro)
            if existente:
                eliminar_libro_db(id_libro)
                print("\n¡Libro eliminado correctamente!")
            else:
                print("\nLibro no encontrado.")
                
        elif opcion == '0':
            print("\n¡Saliendo del sistema de biblioteca. ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Por favor, elegí una opción correcta.")

if __name__ == '__main__':
    ejecutar_sistema()