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