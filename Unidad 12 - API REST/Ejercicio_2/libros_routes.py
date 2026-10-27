from flask import Blueprint, request, jsonify
from conexion import obtener_conexion
from libro_db import obtener_libro_db, insertar_libro_db, actualizar_libro_db, eliminar_libro_db

libros_bp = Blueprint('libros_bp', __name__)

@libros_bp.route('/api/libros', methods=['GET'])
def listar_libros():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio, libros.autor_id, 
            autores.nombre AS autor_nombre, autores.nacionalidad AS autor_nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    """)
    filas = cursor.fetchall()
    conn.close()
    
    libros = [dict(fila) for fila in filas]
    return jsonify(libros), 200

@libros_bp.route('/api/libros/<int:id>', methods=['GET'])
def obtener_libro_por_id(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio, libros.autor_id, 
            autores.nombre AS autor_nombre, autores.nacionalidad AS autor_nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        WHERE libros.id = ?
    """, (id,))
    fila = cursor.fetchone()
    conn.close()
    
    if not fila:
        return jsonify({'error': 'Libro no encontrado'}), 404
        
    return jsonify(dict(fila)), 200

@libros_bp.route('/api/libros', methods=['POST'])
def crear_libro():
    data = request.get_json()
    if not data or 'titulo' not in data or 'anio' not in data or 'autor_id' not in data:
        return jsonify({'error': 'Faltan campos obligatorios (titulo, anio, autor_id)'}), 400
        
    titulo = data['titulo']
    anio = data['anio']
    autor_id = data['autor_id']
    
    nuevo_id = insertar_libro_db(titulo, anio, autor_id)
    libro_creado = obtener_libro_db(nuevo_id)
    return jsonify(libro_creado), 201

@libros_bp.route('/api/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro_existente = obtener_libro_db(id)
    if not libro_existente:
        return jsonify({'error': 'Libro no encontrado'}), 404
        
    data = request.get_json()
    titulo = data.get('titulo', libro_existente['titulo'])
    anio = data.get('anio', libro_existente['anio'])
    autor_id = data.get('autor_id', libro_existente['autor_id'])
    
    actualizar_libro_db(id, titulo, anio, autor_id)
    libro_actualizado = obtener_libro_db(id)
    return jsonify(libro_actualizado), 200

@libros_bp.route('/api/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    libro_existente = obtener_libro_db(id)
    if not libro_existente:
        return jsonify({'error': 'Libro no encontrado'}), 404
        
    eliminar_libro_db(id)
    return jsonify({'mensaje': 'Libro eliminado exitosamente'}), 200