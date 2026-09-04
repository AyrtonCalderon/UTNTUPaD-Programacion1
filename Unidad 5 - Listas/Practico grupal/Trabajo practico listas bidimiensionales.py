#Listas bidimensionales
#=======================================================================
#Ejercicio 1

#=======================================================================
#Ejercicio 2

#=======================================================================
#Ejercicio 3

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
#=======================================================================
#Ejercicio 7

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Extrae matriz[i][i] para cada posición i
diagonal = [matriz[i][i] for i in range(len(matriz))]

print("Diagonal principal:", diagonal)
#=======================================================================
#Ejercicio 8

# Pedimos al usuario el tamaño n de la matriz
n = int(input("Ingrese el tamaño de la matriz identidad (n): "))

# Creamos la matriz vacia
matriz_identidad = []

# Generamos las filas y columnas mediante ciclos anidados
for i in range(n):
    fila = []
    for j in range(n):
        # Si fila == columna estamos en la diagonal principal, ponemos un 1
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    # Agregamos la fila a la matriz
    matriz_identidad.append(fila)

# 4. Mostramos la matriz formateada
print(f"Matriz Identidad de tamaño {n}x{n}:")
for fila in matriz_identidad:
    print(fila)
#=======================================================================
#Ejercicio 9

# Pedimos al usuario el tamaño n de la matriz
n = int(input("Ingrese el tamaño de la matriz (n): "))

# Lista vacía para construir la matriz
matriz_inversa = []

# Recorremos filas y columnas
for i in range(n):
    fila = []
    for j in range(n):
        # La diagonal secundaria cumple que i + j == n - 1
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    matriz_inversa.append(fila)

# Mostramos el resultado
print(f"Matriz Identidad Inversa de tamaño {n}x{n}:")
for fila in matriz_inversa:
    print(fila)
#=======================================================================
#Ejercicio 10
import numpy as np
print("ejercicio 10")
matriz10=np.array([
    [1,2,3],
    [2,4,5],
    [3,5,6]
])
if np.array_equal(matriz10,matriz10.T):
    print("La matriz es simetrica")
else:
    print("La matriz es asimetrica")

#=======================================================================
#Ejercicio 11
print("ejercicio 11")
matriz11=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotado=[]
for i in range(len(matriz11)):
    row=[]
    for j in range(len(matriz11)-1,-1,-1):
        row.append(matriz11[j][i])
    rotado.append(row)
print(rotado)
#=======================================================================
#Ejercicio 12
print("ejercicio 12")
notasString="45, 88, -5, 92, 30, 110, 75, 60, 15"
notas=notasString.split(",")

aprobado=[]
reprobado=[]
notasValidas=[]

for notas in notas:
    notas=int(notas)
    if notas<0 or notas>100:
        continue
    notasValidas.append(notas)
    if notas>=60:
        aprobado.append(notas)
    else:
        reprobado.append(notas)

promedio=sum(notasValidas)/len(notasValidas)

print(f"Aprobados: {aprobado}")
print(f"Reprobados: {reprobado}")
print(f"Promedio: {promedio}")
print(f"Ultimos 2 aprobados: {aprobado[-2:]}")
#=======================================================================
#Ejercicio 13
print("ejercicio 13")
tareas13=[]

while True:
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver resumen")
    print("4. Salir")

    opcion=input("Ingrese una opcion: ")

    if opcion=="1":
        tarea=input("Ingrese el nombre de la tarea: ")

        if tarea in tareas13:
            print("La tarea ya esta registrada")
        else:
            tareas13.append(tarea)
            print("Tarea agregada")

    elif opcion=="2":
        tarea=input("Ingrese el nombre de la tarea a eliminar: ")

        if tarea in tareas13:
            tareas13.remove(tarea)
            print("Tarea eliminada")
        else:
            print("La tarea no existe")

    elif opcion=="3":
        print(f"Total de tareas: {len(tareas13)}")
        print(f"Primeras 3 tareas: {tareas13[:3]}")

    elif opcion=="4":
        print("Programa finalizado")
        break

    else:
        print("Opcion invalida")