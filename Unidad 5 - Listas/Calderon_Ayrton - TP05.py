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

