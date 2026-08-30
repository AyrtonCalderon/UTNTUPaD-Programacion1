#Ejercicio 01

#Genero la lista saltando de 4 en 4
multiplos = list(range(4, 101, 4))

print(multiplos)
#======================================================================
#Ejercicio 02

#--- Crear la lista con 5 elementos
anime = ["Steins-Gate", "Hunter x Hunter", "Fullmetal Alchemist", "Monster", "Ghost in the Shell"]

#--- Accedemos al penultimo elemento usando el indice negativo -2
# En python: -1 es el ultimo elemento y -2 es el penultimo
penultimo = anime[-2]

#---Mostramos el resultado en pantalla
print("La lista completa:", anime)
print("El penúltimo elemento es:", penultimo)

#========================================================
#Ejercicio 03

#Creamos una lista vacIa usando corchetes sin elementos en su interior
mi_lista = []

# Agregamos tres palabras una por una usando el etodo append()
mi_lista.append("Casa")
mi_lista.append("Pizza")
mi_lista.append("Programacion")

# Imprimimos la lista resultante por pantalla
print("La lista resultante es:", mi_lista)

#===================================================================
#Ejercicio 04

# ----Lista inicial de animales
animales = ["perro", "gato", "conejo", "pez"]

# ----Reemplazamos el segundo elemento (indice 1) por "loro"
animales[1] = "loro"

# -----Reemplazamos el ultimo elemento (indice -1) por "oso"
animales[-1] = "oso"

# -----Imprimimos la lista resultante
print("Lista modificada:", animales)

#==========================================================================
#Ejercicio 05
#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# ------Lista original de numeros
numeros = [8, 15, 3, 22, 7]

# ----Busca el numero mas grande (22) y lo elimina de la lista
numeros.remove(max(numeros))

# ---Imprime la lista resultante: [8, 15, 3, 7]
print(numeros)
#==========================================================================
#Ejercicio 06

# --------------Creamos la lista del 10 al 30 de 5 en 5 usando range
# --------------Se usa 31 como limite superior para incluir el 30
numeros = list(range(10, 31, 5))

# -----------------Mostramos los dos primeros elementos usando slicing [0:2]
dos_primeros = numeros[0:2]

# ----------Imprime el resultado
print("Lista completa:", numeros)
print("Los dos primeros elementos son:", dos_primeros)

#==========================================================================
#Ejercicio 07

#----Lista inicial de autos
autos = ["sedan", "polo", "suran", "gol"]

#---------Reemplazamos los elementos en los indices 1 y 2 usando slicing
autos[1:3] = ["corolla", "cronos"]

# ---------Imprimimos la lista resultante
print("Lista modificada:", autos)

#==========================================================
#Ejercicio 08

# --------------------Creamos la lista vacia
dobles = []

# -------------------Agregamos el doble de cada numero directamente con append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# -----------------------Imprimimos la lista resultante
print("Lista de dobles:", dobles)

# Lista inicial de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente (indice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (indice 1, subindice 1)
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente (indice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print("Lista final de compras:", compras)

#==========================================================
#Ejercicio 09
# Lista inicial de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente (indice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (indice 1, subindice 1)
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente (indice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print("Lista final de compras:", compras)

#==========================================================
#Ejercicio 10

#----------------------------Creamos la lista anidada con la estructura indicada
lista_anidada = [
    15,                      # Posicion lista_anidada[0]
    True,                    # Posicion lista_anidada[1]
    [25.5, 57.9, 30.6],      # Posicion lista_anidada[2] (sublista con indices 0, 1 y 2)
    False                    # Posicion lista_anidada[3]
]

# --------------------Imprimimos la lista resultante por pantalla
print(lista_anidada)



