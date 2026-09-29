# ==============================================================================
# PUNTO 1: Lectura del archivo de alumnos
# ==============================================================================

def leer_alumnos():
    lista = []
    try:
        with open("alumnos.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(";")
                if len(partes) == 4:
                    nombre = partes[0]
                    apellido = partes[1]
                    legajo = partes[2]
                    nota = float(partes[3])

                    alumno = {
                        "nombre": nombre,
                        "apellido": apellido,
                        "legajo": legajo,
                        "nota": nota
                    }
                    lista.append(alumno)
    except FileNotFoundError:
        pass
    return lista


# ==============================================================================
# PUNTO 2: Función para validar existencia por legajo
# ==============================================================================

def validar_existe_alumno(legajo, dicc_alumnos):
    return legajo in dicc_alumnos


# ==============================================================================
# PUNTO 3: Carga por teclado y agregado del alumno
# ==============================================================================

def agregar_alumno(lista_alumnos, dicc_alumnos):
    # Validar nombre
    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre.isalpha():
            print("Nombre valido")
            break
        else:
            print("Error: El nombre debe contener solamente letras")

    # Validar apellido
    while True:
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido.isalpha():
            print("Apellido valido.")
            break
        else:
            print("Error: El apellido debe contener unicamente letras.")

    # Validar legajo usando la funcion obligatoria
    while True:
        legajo = input("Ingrese un legajo (5 digitos): ")
        if not legajo.isdigit() or len(legajo) != 5:
            print("Error, el legajo debe ser numerico y tener exactamente 5 digitos")
        elif validar_existe_alumno(legajo, dicc_alumnos):
            print("Error, el legajo ya pertenece a un alumno existente")
        else:
            print("Legajo valido")
            break

    # Validar NOTA
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

    # Crear nuevo alumno
    nuevo_alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "legajo": legajo,
        "nota": nota
    }

    # Actualizo las estructuras en memoria del programa
    lista_alumnos.append(nuevo_alumno)
    dicc_alumnos[legajo] = nuevo_alumno

    # Persistir en alumnos.txt
    with open("alumnos.txt", "a") as archivo:
        linea = f"\n{nombre};{apellido};{legajo};{nota}"
        archivo.write(linea)


# ==============================================================================
# PUNTO 4: Generar archivo de aprobados y mostrar por pantalla
# ==============================================================================

def guardar_aprobados(lista_alumnos):
    print("\n--- ALUMNOS APROBADOS (Nota >= 6) ---")
    with open("aprobados.txt", "w") as archivo_aprobados:
        for alumno in lista_alumnos:
            if alumno["nota"] >= 6:
                linea = f"{alumno['nombre']};{alumno['apellido']};{alumno['legajo']};{alumno['nota']}\n"
                archivo_aprobados.write(linea)
                print(f"{alumno['nombre']} {alumno['apellido']} | Legajo: {alumno['legajo']} | Nota: {alumno['nota']}")


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

# 1. Cargar alumnos desde el archivo
lista_alumnos = leer_alumnos()

# 2. Crear diccionario por legajo
dicc_alumnos = {alumno["legajo"]: alumno for alumno in lista_alumnos}

# 3. Pedir datos y agregar nuevo alumno
agregar_alumno(lista_alumnos, dicc_alumnos)

# 4. Mostrar listado completo en consola
print("\n--- LISTADO COMPLETO DE ALUMNOS EN MEMORIA ---")
for alu in lista_alumnos:
    print(f"{alu['nombre']} {alu['apellido']} | Legajo: {alu['legajo']} | Nota: {alu['nota']}")

# 5. Exportar y mostrar aprobados
guardar_aprobados(lista_alumnos)





