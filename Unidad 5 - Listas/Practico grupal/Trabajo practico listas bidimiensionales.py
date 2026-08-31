#Listas bidimensionales
#=======================================================================
#Ejercicio 4

#--Definimos la matriz original (2 filas x 3 columnas)
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

#-- Obtenemos las dimensiones de la matriz original
filas = len(matriz)           # Numero de filas (2)
columnas = len(matriz[0])     # Numero de columnas (3)

# -- Creamos la matriz transpuesta vacia con dimensiones invertidas.
# La original era 2 x 3, la transpuesta sera de 3 filas x 2 columnas.
# La llenamos temporalmente con ceros.

transpuesta = []
for j in range(columnas):
    fila_nueva = []
    for i in range(filas):
        fila_nueva.append(0)
    transpuesta.append(fila_nueva)

#-- Recorremos la matriz original para copiar los valores invertidos
for i in range(filas):
    for j in range(columnas):
        # El elemento en la posicion [i][j] de la matriz original
        # pasa a la posición [j][i] en la matriz transpuesta.
        transpuesta[j][i] = matriz[i][j]

#--Mostramos el resultado en pantalla
print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)

#======================================================
#Ejercicio 5
#----Definimos la matriz con valores de prueba
matriz = [
    [11, 43, 74],
    [52, 85, 22],
    [64, 81, 12]
]

#-------Inicializamos el mayor con el primer elemento de la matriz (posicion [0][0])
mayor = matriz[0][0]

# -----Recorremos todas las filas y columnas mediante ciclos anidados
for fila in matriz:
    for elemento in fila:
        # Si el elemento actual es mas grande que el que teniamos guardado, actualizamos 'mayor'
        if elemento > mayor:
            mayor = elemento

# ------Mostramos la matriz y el resultado final
print("Matriz:")
for fila in matriz:
    print(fila)

print(f"El valor más grande en la lista bidimensional es: {mayor}")

#============================================================================
#Ejercicio 6

# -----------Definimos la matriz original
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

#----------Pedimos al usuario el valor escalar y lo convertimos a entero o flotante
escalar = int(input("Ingrese el número escalar por el que desea multiplicar: "))

# -------------Obtenemos las dimensiones
filas = len(matriz)
columnas = len(matriz[0])

# ------------Creamos una nueva matriz vacía con el mismo tamaño para guardar el resultado
matriz_resultante = []

# -------------Recorremos la matriz original para realizar la multiplicacion
for i in range(filas):
    nueva_fila = []
    for j in range(columnas):
        # Multiplicamos el elemento actual por el escalar
        nuevo_valor = matriz[i][j] * escalar
        nueva_fila.append(nuevo_valor)
    # Agregamos la fila terminada a la matriz resultante
    matriz_resultante.append(nueva_fila)

# 6. Mostramos los resultados
print("Matriz Original:")
for fila in matriz:
    print(fila)

print(f"Matriz multiplicada por {escalar}:")
for fila in matriz_resultante:
    print(fila)