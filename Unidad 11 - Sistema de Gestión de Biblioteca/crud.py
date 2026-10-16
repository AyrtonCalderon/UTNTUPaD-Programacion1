import sqlite3


def conectar_db():
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    return conexion, cursor


def registrar_autor(nombre, nacionalidad):
    conexion, cursor = conectar_db()
    cursor.execute(
        "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
        (nombre, nacionalidad),
    )
    autor_id = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return autor_id


def registrar_libro(titulo, anio, autor_id):
    conexion, cursor = conectar_db()
    cursor.execute(
        "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
        (titulo, anio, autor_id),
    )
    conexion.commit()
    conexion.close()


def listar_libros():
    conexion, cursor = conectar_db()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    """)
    resultados = cursor.fetchall()
    conexion.close()

    print("\n--- LISTADO DE LIBROS EN LA BIBLIOTECA ---")
    for fila in resultados:
        id_l, titulo, anio, nombre_a, nac_a = fila
    print(
        f"ID: {id_l} | Libro: '{titulo}' ({anio}) | Autor: {nombre_a} [{nac_a}]"
    )

    return resultados


def actualizar_titulo_libro(id_libro, nuevo_titulo):
    conexion, cursor = conectar_db()
    cursor.execute(
        "UPDATE libros SET titulo = ? WHERE id = ?", (nuevo_titulo, id_libro)
    )
    conexion.commit()
    conexion.close()
    print(f"¡Libro con ID {id_libro} actualizado con éxito!")


def eliminar_libro(id_libro):
    conexion, cursor = conectar_db()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    conexion.close()
    print(f"Libro con ID {id_libro} eliminado de la base de datos")