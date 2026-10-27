from conexion import obtener_conexion

def obtener_autores_db():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autores")
    filas = cursor.fetchall()
    conn.close()
    return [dict(fila) for fila in filas]

def obtener_autor_db(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autores WHERE id = ?", (id,))
    fila = cursor.fetchone()
    conn.close()
    return dict(fila) if fila else None

def insertar_autor_db(nombre, nacionalidad):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)", (nombre, nacionalidad))
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()
    return nuevo_id