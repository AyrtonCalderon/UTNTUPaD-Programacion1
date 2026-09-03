#Tipos de valor inmutables (Enteros)
def duplicar(x):
    x= x * 2
    print("Dentro de la funcion:", x)

a=10
duplicar(a)
print("Fuera de la funcion:", a)

def agregar_elementos(lista):
    lista.append(4)
    print("Dentro de la funcion:", lista)

mi_lista = [1, 2, 3]
agregar_elementos(mi_lista)
print("Fuera de la funcion:", mi_lista)

#Modificacion de listas

#PASO INMUTABLE
def modificar_valor(x):
    print("Dentro de la funcion antes de reasignar: ", x)

    x = 20
    print("Dentro de la funcion despues de reasignar:", x)

a=10
modificar_valor(a)
print("Fuera de la funcion:", a)

#PASO MUTABLE
def modificar_lista(lista):
    print("Dentro de la funcion antes de modificar: ", lista)
    lista.append(4)
    print("Dentro de la funcion despues de modificar: ", lista)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la funcion:", mi_lista)

#Reasignacion
def reasignar_lista(lista):
    print("Dentro de la funcion antes de reasignar:", lista)
    lista = [4, 4 , 4]
    print("Dentro de la funcion despues de reasignar:", lista)

mi_lista = [1, 2, 3]
reasignar_lista(mi_lista)
print("Fuera de la funcion:", mi_lista)

#Lista de listas

def agregar_elementos(matriz):
    matriz[0].append(99)
    matriz.append([4, 5, 6])

matriz = [[1, 2 ], [3, 4]]
agregar_elementos(matriz)
print("Matriz final:", matriz)

#Reasignacion de lista
def reemplazar_sublista(matriz):
    matriz[0] = [0, 0, 0] #Reasignacion interna, reemplaza la referencia 

matriz= [[1, 2] , [3, 4]]
reemplazar_sublista(matriz)
print("Matriz modificada:", matriz)

#Comparacion 
def operar_lista(lst):
    lst.append(10) #Modificar objeto original
    lst = [0, 0, 0] #Reasignar la variable original

lista = [1, 2, 3]
operar_lista(lista)
print("Lista final:", lista)

#Clonacion
import copy

def modificar_listas(original, copia_superficial, copia_deep):
    original[0] [0]="X"
    copia_superficial[0] [1]= "Y"
    copia_deep[0] [2]= "Z"


data = [[1, 2, 3], [4, 5, 6]]
copia_superficial = copy.copy(data)
copia_Prof = copy.deepcopy(data)

modificar_listas(data , copia_superficial , copia_Prof)

print("Original: ", data)
print("Copia superficial: ", copia_superficial)
print("Copia profunda: ", copia_Prof)



