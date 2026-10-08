from nota import Nota

class Alumno:
    def __init__(self, nombreCompleto: str, legajo: int):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo 
        self.notas = []

    def agregar_nota(self, nota: Nota):
        self.notas.append(nota)

    def calcular_promedio(self) -> float:
        if len(self.notas) == 0:
            return 0.0
        suma = 0
        for n in self.notas:
            suma += n.nota_examen
        return suma / len(self.notas)