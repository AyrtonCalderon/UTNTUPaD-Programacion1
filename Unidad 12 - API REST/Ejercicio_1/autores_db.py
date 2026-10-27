from conexion import obtener_conexion

def obtener_autores_db():
    """Trae todos los autores de la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autores")
    filas = cursor.fetchall()
    conn.close()
    return [dict(fila) for fila in filas]

def obtener_autor_db(id):
    """Trae un autor específico por su ID."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autores WHERE id = ?", (id,))
    fila = cursor.fetchone()
    conn.close()
    return dict(fila) if fila else None

def insertar_autor_db(nombre, nacionalidad):
    """Inserta un nuevo autor y retorna su ID generado."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)", (nombre, nacionalidad))
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()
    return nuevo_id