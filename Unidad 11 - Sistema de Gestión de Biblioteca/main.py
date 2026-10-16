from base_datos import inicializar_base_datos
from crud import (
    actualizar_titulo_libro,
    eliminar_libro,
    listar_libros,
    registrar_autor,
    registrar_libro,
)


def pedir_texto(mensaje):
  """Función auxiliar para asegurar que el usuario no deje el campo vacío"""
  while True:
    texto = input(mensaje).strip()
    if texto:
      return texto
    print("El campo no puede estar vacío. Por favor, intente de nuevo.")


def menu():
  # Inicializamos la base de datos al arrancar
  inicializar_base_datos()

  while True:
    print("\n==========================================")
    print("     SISTEMA DE GESTIÓN DE BIBLIOTECA     ")
    print("==========================================")
    print("1. Registrar un autor")
    print("2. Registrar un libro")
    print("3. Listar todos los libros")
    print("4. Actualizar el título de un libro")
    print("5. Eliminar un libro")
    print("6. Salir")

    opcion = input("\nElige una opción (1-6): ").strip()

    if opcion == "1":
      print("\n--- Registrar Autor ---")
      nombre = pedir_texto("Nombre del autor: ")
      nacionalidad = pedir_texto("Nacionalidad: ")
      id_autor = registrar_autor(nombre, nacionalidad)
      print(f"¡Autor registrado con éxito! ID asignado: {id_autor}")

    elif opcion == "2":
      print("\n--- Registrar Libro ---")
      titulo = pedir_texto("Título del libro: ")
      while True:
        try:
          anio = int(input("Año de publicación: "))
          break
        except ValueError:
          print("Error: El año debe ser un número entero válido.")

      while True:
        try:
          autor_id = int(input("ID del autor correspondiente: "))
          break
        except ValueError:
          print("Error: El ID del autor debe ser un número entero.")

      registrar_libro(titulo, anio, autor_id)
      print("¡Libro registrado con éxito!")

    elif opcion == "3":
      listar_libros()

    elif opcion == "4":
      print("\n--- Actualizar Título de Libro ---")
      while True:
        try:
          id_libro = int(input("ID del libro a actualizar: "))
          break
        except ValueError:
          print(" Error: El ID debe ser un número entero.")
      nuevo_titulo = pedir_texto("Nuevo título: ")
      actualizar_titulo_libro(id_libro, nuevo_titulo)

    elif opcion == "5":
      print("\n--- Eliminar Libro ---")
      while True:
        try:
          id_libro = int(input("ID del libro a eliminar: "))
          break
        except ValueError:
          print("Error: El ID debe ser un número entero.")
      eliminar_libro(id_libro)

    elif opcion == "6":
      print("\n¡Saliendo del sistema de biblioteca. ¡Hasta luego!")
      break
    else:
      print(" Opción no válida. Por favor, elegí un número del 1 al 6.")


if __name__ == "__main__":
  menu()