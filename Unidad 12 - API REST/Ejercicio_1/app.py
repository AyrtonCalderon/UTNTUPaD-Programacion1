from flask import Flask, jsonify, request
from libro_db import (
    obtener_libros_db, obtener_libro_db,
    insertar_libro_db, actualizar_libro_db, eliminar_libro_db
)
from models import Libro

app = Flask(__name__)

# 1. GET: Obtener todos los libros
@app.route('/api/libros', methods=['GET'])
def get_libros():
    filas = obtener_libros_db()
    lista = []
    for f in filas:
        # Usamos 'Libro' con mayúscula y accedemos por nombre gracias a sqlite3.Row
        libro_obj = Libro(id_libro=f['id'], titulo=f['titulo'], año=f['año'], autor_id=f['autor_id'])
        lista.append(libro_obj.a_diccionario())
    return jsonify(lista), 200

# 2. GET: Obtener un libro por ID
@app.route('/api/libros/<int:id>', methods=['GET'])
def get_libro(id):
    f = obtener_libro_db(id)
    if f:
        libro_obj = Libro(id_libro=f['id'], titulo=f['titulo'], año=f['año'], autor_id=f['autor_id'])
        return jsonify(libro_obj.a_diccionario()), 200
    return jsonify({"error": "Libro no encontrado"}), 404

# 3. POST: Crear un nuevo libro
@app.route('/api/libros', methods=['POST'])
def post_libro():
    datos = request.get_json()
    if not datos or 'titulo' not in datos or 'año' not in datos or 'autor_id' not in datos:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    
    nuevo_id = insertar_libro_db(datos['titulo'], datos['año'], datos['autor_id'])
    libro_obj = Libro(id_libro=nuevo_id, titulo=datos['titulo'], anio=datos['año'], autor_id=datos['autor_id'])
    return jsonify(libro_obj.a_diccionario()), 201

# 4. PUT: Actualizar un libro
@app.route('/api/libros/<int:id>', methods=['PUT'])
def put_libro(id):
    existente = obtener_libro_db(id)
    if not existente:
        return jsonify({"error": "Libro no encontrado"}), 404
        
    datos = request.get_json()
    titulo = datos.get('titulo', existente['titulo'])
    año = datos.get('año', existente['año'])
    autor_id = datos.get('autor_id', existente['autor_id'])
    
    actualizar_libro_db(id, titulo, año , autor_id)
    return jsonify({"mensaje": "Libro actualizado correctamente"}), 200

# 5. DELETE: Eliminar un libro
@app.route('/api/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
    existente = obtener_libro_db(id)
    if not existente:
        return jsonify({"error": "Libro no encontrado"}), 404
        
    eliminar_libro_db(id)
    return jsonify({"mensaje": "Libro eliminado correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)