# ==============================================================================
# PUNTO 1: Inicialización de estructuras y lectura del archivo de alumnos
# ==============================================================================

# Creo la lista general para guardar diccionarios y el diccionario por legajo
lista_alumnos = []
dicc_alumnos = {}

# Abrimos el archivo en modo lectura ("r") desde la subcarpeta correspondiente
with open("Unidad 7 - Datos complejos/alumnos.txt", "r") as archivo:
    for linea in archivo:
        # Limpio saltos de linea y separo los datos por el delimitador ";"
        partes = linea.split(";")

        # Asignar cada elemento a su variable
        nombre = partes[0]
        apellido = partes[1]
        legajo = partes[2]
        nota = float(partes[3]) # Convierto texto a decimal

        # Guardo la informacion en la estructura del programa
        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "legajo": legajo,
            "nota": nota
        }

        # Agrego a las estructuras dentro del ciclo
        lista_alumnos.append(alumno)
        dicc_alumnos[legajo] = alumno

# ==============================================================================
# PUNTO 2: Carga por teclado con validaciones en ciclos de repetición
# ==================================================================================

#Valido nombre

while True:
    nombre = input("Ingrese el nombre del alumno: ")
    if nombre.isalpha():
        print("Nombre valido")
        break #Sale del ciclo solo si es valido
    else:
        print("Error: El nombre debe contener solamente letras")

#Validar apellido
while True:
    apellido = input("Ingrese el apellido del alumno: ")
    if apellido.isalpha():
        print("Apellido valido.")
        break
    else:
        print("Error: El apellido debe contener unicamente letras.")

#Validar legajo
while True:
    legajo = input("Ingrese un legajo (5 digitos): ")
    
    if not legajo.isdigit() or len(legajo) != 5:
        print("Error, el legajo debe ser numerico y tener exactamente 5 digitos")
    elif legajo in dicc_alumnos:
        print("Error, el legajo ya pertenece a un alumno existente")
    else:
        print("Legajo valido")
        break

#Validar NOTA (decimal dentro del rango de 1 a 10 con manejo de excepciones)
while True:
    try:
        nota = float(input("Ingrese la nota promedio (del 1 al 10): "))
        if 1 <= nota <= 10:
            print("Nota valida")
            break
        else:
            print("Error, la nota debe estar entre 1 y 10")
    except ValueError:
        print("Error, debe ingresar un numero valido")


# =================================================================================
# PUNTO 3: Guardar el nuevo alumno y generar el archivo de aprobados
# ===============================================================================

#Nuevo alumno
nuevo_alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "legajo": legajo,
    "nota": nota
}

#Actualizo las estructuras en memoria del programa
lista_alumnos.append(nuevo_alumno)
dicc_alumnos[legajo] = nuevo_alumno

## Abrimos el archivo en modo agregar ("a") para persistir el nuevo registro
with open("Unidad 7 - Datos complejos/alumnos.txt", "a") as archivo:
    linea = f"\n{nombre};{apellido};{legajo};{nota}"
    archivo.write(linea)

# Abrimos (o creamos) "aprobados.txt" en modo escritura ("w") para actualizar la lista de aprobados
with open("aprobados.txt", "w") as archivo_aprobados:
    for alumno in lista_alumnos:
        if alumno["nota"] >= 6:
            linea = f"{alumno['nombre']};{alumno['apellido']};{alumno['legajo']};{alumno['nota']}\n"
            archivo_aprobados.write(linea)





