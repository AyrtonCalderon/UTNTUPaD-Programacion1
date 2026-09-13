#Ejercicio B

# 1. Diccionario de alumnos (Legajo: "Apellido Nombre")

alumnos = {
    60920: "Fernandez Rodolfo" ,
    61654: "Luis Gomez" ,
    61852: "Andrea Pereira" ,
    61754: "Juan Cruz Gonzales"
}

#2. Lista de materias de dos dimensiones

# Matriz / Lista Bidimensional de Materias
# [
#   [Materia, Nota 1, Nota 2, Nota Final],
#   ...
# ]
materias = [
            ["Matematica" , 0 , 0 , 0.0] ,
            ["Historia", 0 , 0 , 0.0] ,
            ["Geografia", 0 , 0 , 0.0] ,
            ["Ciencias", 0 , 0 , 0.0] ,
            ["Fisica" , 0 , 0 , 0.0]
]
.
# 3. Lista notasFinales (Bidimensional)
# [
#   [Nombre_Alumno, Promedio_General],
#   ...
# ]

# Creamos la lista vacía para guardar los promedios generales
notasFinales = []

# Recorremos el diccionario de alumnos (Legajo y Nombre)
for legajo,nombre in alumnos.items():
    print(f"{nombre}")
    suma_promedio_materias = 0 # Para acumular las notas del alumno

#Por cada alumno, recorremos la lista de materias
for mat in materias:
    nombre_materia = mat[0]
    print(f"Ingrese las notas para {nombre_materia}: ")

    # Pedir Nota 1 con validación (0 al 10)
    nota_1 = float(input("Nota 1: "))
    while nota_1 < 0 or nota_1 > 10:
        print("Error, la nota ingresada debe ser del 0 al 10")
        nota1 = float(input("Nota 1: "))

    # Pedir Nota 2 con validación (0 al 10)
        nota2 = float(input("Nota 2: "))
        while nota2 < 0 or nota2 > 10:
            print("Error, la nota ingresada debe ser del 0 al 10")
            nota2 = float(input("Nota 2: "))

        # Calcular el promedio de esta materia
        promedio_materia = (nota1 + nota2) / 2
        print(f"Nota Final en {nombre_materia}: {promedio_materia}")

        # Acumulamos para el promedio general del alumno
        suma_promedios_materias += promedio_materia

    # 4. Al terminar todas las materias del alumno, calculamos su promedio general
    promedio_general = suma_promedios_materias / len(materias)

    # 5. Guardamos [Nombre, Promedio General] en la lista notasFinales
    notasFinales.append([nombre, promedio_general])



