#Ejercicio B

# 1. Funcion para validar el ingreso de notas (evita repetir el while)
def pedir_nota_valida(mensaje):
    nota = float(input(mensaje))
    while nota < 0 or nota > 10:
        print("Error, la nota ingresada debe ser del 0 al 10")
        nota = float(input(mensaje))
    return nota

# 2. Funcion principal que procesa a los alumnos
def cargar_notas_alumnos(alumnos, materias):
    notasFinales = []
    
    for legajo, nombre in alumnos.items():
        print(f"\n Alumno: {nombre} ")
        suma_promedio_materia = 0

        for mat in materias:
            nombre_materia = mat[0]
            print(f"Ingrese las notas para {nombre_materia}:")

            nota_1 = pedir_nota_valida("Nota 1: ")
            nota_2 = pedir_nota_valida("Nota 2: ")

            promedio_materia = (nota_1 + nota_2) / 2
            print(f"Nota Final en {nombre_materia}: {promedio_materia}")

            suma_promedio_materia += promedio_materia

        promedio_general = suma_promedio_materia / len(materias)
        notasFinales.append([nombre, promedio_general])
        
    return notasFinales


# --- Datos de prueba ---
alumnos = {
    60920: "Fernandez Rodolfo",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

materias = [
    ["Matematica", 0, 0, 0.0],
    ["Historia", 0, 0, 0.0],
    ["Geografia", 0, 0, 0.0],
    ["Ciencias", 0, 0, 0.0],
    ["Fisica", 0, 0, 0.0]
]

# --- Llamada a la función ---
resultados = cargar_notas_alumnos(alumnos, materias)
print("\nNotas Finales:", resultados)



