import sqlite3

def obtener_conexion():
    """Establece y retorna una conexión a la base de datos SQLite."""
    conn = sqlite3.connect('biblioteca.db') # O el nombre de tu base de datos (ej. biblioteca.db o el que estés usando)
    conn.row_factory = sqlite3.Row  # Esto es clave para poder usar los resultados como diccionarios
    return conn