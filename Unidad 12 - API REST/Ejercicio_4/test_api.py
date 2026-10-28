import requests

# URL base de tu API Flask
BASE_URL = "http://127.0.0.1:5000/api"


def ejecutar_pruebas():
    print("=== INICIO DE PRUEBAS AUTOMATIZADAS DE LA API ===")

try:
    # 1. Hacer GET a /libros
    print("\n--- 1. Probando GET /libros ---")
    response = requests.get(f"{BASE_URL}/libros")
    print(f"Status Code: {response.status_code}")
    print("Listado actual de libros:", response.text)

    # 2. Hacer POST para crear un autor y luego un libro
    print("\n--- 2. Probando POST (Crear Autor y Libro) ---")

    autor_data = {"nombre": "Isabel Allende", "nacionalidad": "Chilena"}
    res_autor = requests.post(f"{BASE_URL}/autores", json=autor_data)
    print(f"Crear Autor - Status Code: {res_autor.status_code}")
    print("Respuesta Autor:", res_autor.text)

    # Obtenemos el ID del autor recién creado de forma segura
    autor_id = None
    try:
        autor_id = res_autor.json().get("id")
    except Exception:
        pass

    if not autor_id:
        autores = requests.get(f"{BASE_URL}/autores").json()
        if autores:
            autor_id = autores[-1]["id"]

    # Creamos el libro asociado a ese autor
    libro_data = {
        "titulo": "La casa de los espíritus",
        "anio": 1982,
        "autor_id": autor_id,
    }
    res_libro = requests.post(f"{BASE_URL}/libros", json=libro_data)
    print(f"Crear Libro - Status Code: {res_libro.status_code}")
    print("Respuesta Libro:", res_libro.text)

    # Obtenemos el ID del libro recién creado de forma segura
    libro_id = None
    try:
        libro_id = res_libro.json().get("id")
    except Exception:
        pass

    if not libro_id:
        libros = requests.get(f"{BASE_URL}/libros").json()
        if libros:
            libro_id = libros[-1]["id"]

    # 3. Hacer PUT para actualizar el título del libro recién creado
    print(f"\n--- 3. Probando PUT (Actualizar Libro ID: {libro_id}) ---")
    update_data = {
        "titulo": "La casa de los espíritus (Edición Especial)",
        "anio": 1982,
        "autor_id": autor_id,
    }
    res_put = requests.put(f"{BASE_URL}/libros/{libro_id}", json=update_data)
    print(f"Actualizar Libro - Status Code: {res_put.status_code}")
    print("Respuesta PUT:", res_put.text)

    # 4. Hacer DELETE para eliminar el libro creado
    print(f"\n--- 4. Probando DELETE (Eliminar Libro ID: {libro_id}) ---")
    res_del = requests.delete(f"{BASE_URL}/libros/{libro_id}")
    print(f"Eliminar Libro - Status Code: {res_del.status_code}")
    print("Respuesta DELETE:", res_del.text)

    print("\n=== FIN DE LAS PRUEBAS AUTOMATIZADAS ===")

except requests.exceptions.ConnectionError:
    print(
        "\n[ERROR DE CONEXIÓN] No se pudo conectar con el servidor. Asegurate"
        " de tener Flask encendido."
    )


if __name__ == "__main__":
    ejecutar_pruebas()