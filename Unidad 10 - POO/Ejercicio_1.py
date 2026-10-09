#PROGRAMACION ORIENTADA A OBJETOS

# Ejercicio 1

# ============================================================
# CLASE CELDA
# ============================================================

class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor


# ============================================================
# CLASE MATRIZ
# ============================================================

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    # Metodo para buscar una celda
    def buscar_celda(self, fila, columna):

        for c in self.celdasMatriz:

            if c.fila == fila and c.columna == columna:
                return c.valor

        return "La fila y columna indicada no ha sido asignada en ninguna celda"


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

mi_matriz = Matriz()


while True:

    # --------------------------------------------------------
    # PEDIMOS EL VALOR
    # --------------------------------------------------------

    valor = input("Ingrese un valor para la celda (o FIN para terminar): ").strip()

    # Si esta vacio, volvemos a pedirlo
    if valor == "":
        print("Error: debe ingresar un valor.")
        continue

    # Si escribe FIN, terminamos
    if valor.upper() == "FIN":
        break


    # --------------------------------------------------------
    # PEDIMOS LA FILA
    # --------------------------------------------------------

    while True:

        try:
            fila = int(input("Ingrese numero de fila: "))

            # Validamos que sea mayor que 0
            if fila <= 0:
                print("Error: la fila debe ser mayor que 0.")
                continue

            break

        except ValueError:
            print("Error: debe ingresar un numero entero.")


    # --------------------------------------------------------
    # PEDIMOS LA COLUMNA
    # --------------------------------------------------------

    while True:

        try:
            columna = int(input("Ingrese numero de columna: "))

            # Validamos que sea mayor que 0
            if columna <= 0:
                print("Error: la columna debe ser mayor que 0.")
                continue

            break

        except ValueError:
            print("Error: debe ingresar un numero entero.")


    # --------------------------------------------------------
    # VALIDAMOS SI LA POSICION YA EXISTE
    # --------------------------------------------------------

    existe = False

    for c in mi_matriz.celdasMatriz:

        if c.fila == fila and c.columna == columna:
            existe = True
            break


    # --------------------------------------------------------
    # SI EXISTE, NO LA GUARDAMOS
    # --------------------------------------------------------

    if existe:

        print("Error: ya existe una celda cargada en esa fila y columna.")


    # --------------------------------------------------------
    # SI NO EXISTE, CREAMOS LA CELDA
    # --------------------------------------------------------

    else:

        nueva_celda = Celda(fila, columna, valor)

        mi_matriz.celdasMatriz.append(nueva_celda)

        print("Celda guardada correctamente.")


# ============================================================
# MOSTRAMOS LAS CELDAS CARGADAS
# ============================================================

print("\n--- CELDAS CARGADAS ---")

if len(mi_matriz.celdasMatriz) == 0:

    print("No se cargaron celdas.")

else:

    for c in mi_matriz.celdasMatriz:

        print(
            f"Fila: {c.fila}, "
            f"Columna: {c.columna}, "
            f"Valor: {c.valor}"
        )


# ============================================================
# BUSCAMOS UNA CELDA
# ============================================================

print("\n--- BUSCAR CELDA ---")


# Pedimos fila a buscar
while True:

    try:
        fila_buscar = int(input("Ingrese la fila que desea buscar: "))

        if fila_buscar <= 0:
            print("Error: la fila debe ser mayor que 0.")
            continue

        break

    except ValueError:
        print("Error: debe ingresar un numero entero.")


# Pedimos columna a buscar
while True:

    try:
        columna_buscar = int(input("Ingrese la columna que desea buscar: "))

        if columna_buscar <= 0:
            print("Error: la columna debe ser mayor que 0.")
            continue

        break

    except ValueError:
        print("Error: debe ingresar un numero entero.")


# Usamos el metodo de la clase Matriz
resultado = mi_matriz.buscar_celda(fila_buscar, columna_buscar)

print("Resultado:", resultado)

#=================================================================



            
    










