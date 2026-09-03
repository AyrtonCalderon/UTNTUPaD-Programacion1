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