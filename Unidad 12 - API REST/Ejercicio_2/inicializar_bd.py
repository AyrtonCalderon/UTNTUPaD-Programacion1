import sqlite3

# Conecta directamente a tu base de datos existente
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Crear tabla autores
cursor.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        nacionalidad TEXT NOT NULL
    )
""")

# Crear tabla libros
cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        anio INTEGER,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES autores (id)
    )
""")

conn.commit()
conn.close()
print("¡Tablas creadas exitosamente en biblioteca.db!")