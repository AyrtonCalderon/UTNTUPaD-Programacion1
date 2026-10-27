from conexion import obtener_conexion

def obtener_libros_db():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros")
    filas = cursor.fetchall()
    conn.close()
    return [dict(fila) for fila in filas]

def obtener_libro_db(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros WHERE id = ?", (id,))
    fila = cursor.fetchone()
    conn.close()
    return dict(fila) if fila else None

def insertar_libro_db(titulo, anio, autor_id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)", (titulo, anio, autor_id))
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()
    return nuevo_id

def actualizar_libro_db(id, titulo, anio, autor_id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE libros 
        SET titulo = ?, anio = ?, autor_id = ? 
        WHERE id = ?
    """, (titulo, anio, autor_id, id))
    conn.commit()
    conn.close()

def eliminar_libro_db(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id,))
    conn.commit()
    conn.close()