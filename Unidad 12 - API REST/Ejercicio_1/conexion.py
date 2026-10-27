#Este archivo se encarga únicamente de abrir la conexión con la base de datos aplicando tu lógica de sqlite3.Row
import sqlite3

DATABASE = 'biblioteca.db'

def obtener_conexion():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conn

