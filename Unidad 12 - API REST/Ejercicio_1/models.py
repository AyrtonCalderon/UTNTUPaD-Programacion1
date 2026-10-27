class Libro:
    def __init__(self, id_libro, titulo, año, autor_id):
        self.id_libro = id_libro
        self.titulo = titulo
        self.año = año
        self.autor_id = autor_id

    def a_diccionario(self):
        return {
            "id": self.id_libro,
            "titulo": self.titulo,
            "año": self.año,
            "autor_id": self.autor_id
        }
    