from flask import Blueprint, request, jsonify
from autores_db import obtener_autores_db, obtener_autor_db, insertar_autor_db

autores_bp = Blueprint('autores_bp', __name__)

@autores_bp.route('/api/autores', methods=['GET'])
def listar_autores():
    autores = obtener_autores_db()
    return jsonify(autores), 200

@autores_bp.route('/api/autores', methods=['POST'])
def crear_autor():
    data = request.get_json()
    if not data or 'nombre' not in data or 'nacionalidad' not in data:
        return jsonify({'error': 'Faltan campos obligatorios (nombre, nacionalidad)'}), 400
        
    nombre = data['nombre']
    nacionalidad = data['nacionalidad']
    
    nuevo_id = insertar_autor_db(nombre, nacionalidad)
    autor_creado = obtener_autor_db(nuevo_id)
    return jsonify(autor_creado), 201