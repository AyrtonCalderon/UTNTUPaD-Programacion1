# Lista de una dimension

# Actividad 1: Escribe un programa que permita al usuario ingresar una lista de numeros y calcule la suma de todos los elementos en la lista.
cantidad_de_elementos = int(input("Ingrese la cantidad de elementos que desea agregar a su lista: "))
lista = []
for contador in range(cantidad_de_elementos):
    print("Ingrese el valor: ")
    lista.append(int(input()))
print(f"La suma de la lista es: {sum(lista)}")

#Actividad 2: Escribe un programa que pida al usuario una lista de numeros y encuentre el mayor y el menor de ellos. 
cantidad_de_elementos = int(input("Ingrese la cantidad de elementos que desea agregar a su lista: "))
lista =[]
for contador in range(cantidad_de_elementos):
    print("Ingrese el valor: ")
    lista.append(int(input()))
print(f"El número mayor de la lista es {max(lista)} y el número menor es {min(lista)}")

# Actividad 3: Escribe un programa que permita al usuario ingresar una lista y la invierta. 
cantidad_de_elementos = int(input("Ingrese la cantidad de elementos que desea agregar a su lista: "))
lista =[]
for contador in range(cantidad_de_elementos):
    print("Ingrese el valor: ")
    lista.append(int(input()))
lista.reverse()
print(lista)

# Actividad 4: Escribe un programa que pida al usuario una lista de números y cuente cuántos de ellos son pares y cuántos son impares. 
# Pedir ingreso de datos
entrada = input("Ingrese numeros enteros separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
# Contar pares e impares
pares = sum(1 for x in numeros if x % 2 == 0)
impares = len(numeros) - pares
# Mostrar resultados
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)

# Actividad 5: Escribe un programa que multiplique cada elemento de una lista de números por un valor ingresado por el usuario. 
# Pedir lista de numeros y factor de multiplicacion
entrada = input("Ingrese numeros separados por espacios: ")
numeros = [float(x) for x in entrada.split()]
factor = float(input("Ingrese el numero por el cual desea multiplicar: "))

# Multiplicar cada elemento
resultado = [x * factor for x in numeros]
# Mostrar resultado
print("Lista multiplicada:", resultado)

# Actividad 6: Escribe un programa que permita al usuario ingresar una lista de números y elimine lo elementos duplicados.
# Pedir ingreso de datos
entrada = input("Ingrese numeros separados por espacios: ")
numeros = [float(x) for x in entrada.split()]
# Convertir a conjunto para eliminar repetidos y reconvertir a lista
sin_duplicados = list(set(numeros))
# Mostrar resultado
print("Lista sin duplicados:", sin_duplicados)

# Actividad 7: Escribe un programa que permita al usuario ingresar una lista de números y calcule el promedio de los elementos.
# Pedimos al usuario que ingresse numeros separados por espacios
entrada = input("Ingrese numeros separados por espacios:")
# Convertimos la entrada en una lista de enteros
lista = list(map(int, entrada.split()))
# Calculamos la suma de todos los numeros 
suma = sum(lista)
# Calculamos el promedio
promedio = suma / len(lista)
# Mostramos el promedio
print("El promedio es:", promedio)

# Actividad 8: Escribe un programa que identifique y muestre los elementos que se repiten en una lista. 
# Pedimos al usuario que ingrese numeros separados por espacios
entrada = input("Ingrese los numeros separados por espacios:")
# Convertimos los numeros ingresados en una lista de enteros
lista = list(map(int,entrada.split()))
# Creamos un conjunto para guardar los elementos repetidos
repetidos = set()
# Recorremos cada elemento de la lista 
for elemento in lista:
    # Contamos cuantas veces aparece el elemento
    if lista.count(elemento) > 1:
        # Agregamos el elemento al conjunto de repetidos
        repetidos.add(elemento)
# Mostramos los elementos repetidos
print("Los elementos repetidos son:", repetidos)

# Actividad 9: Escribe un programa que permita al usuario ingresar una lista de números y filtre los números primos. 
# Creamos una funcion para verificar si un numero es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
# Pedimos al usuario que ingrese numeros separados por espacios
entrada = input("Ingrese numeros separados por espacios:")
# Convertimos los numeros ingresados en una lista de enteros
lista = list(map(int,entrada.split()))
# Creamos una lista vacia para guardar los numeros primos
primos = []
# Recorremos los numeros de la lista
for numero in lista:
    # Verificamos si el numero es primo
    if es_primo(numero):
        # Agregamos el numero a la lista de primos
        primos.append(numero)
# Mostramos los numeros primos encontrados
print("Los numeros primos son:", primos)

# Actividad 10: Escribe un programa que permita al usuario ingresar una lista de números y eliminar un elemento en un índice especificado. 
# Pedimos al usuario que ingrese numeros separados por espacios
entrada = input("Ingrese numeros separados por espacios:")
# Convertimos los numeros en una lista de enteros
lista = list(map(int,entrada.split()))
# Pedimos al usuario que ingrese el indice del elemento a eliminar
indice = int(input("Ingrese el indice del elemento que desea eliminar:"))
# Verificamos si el indice es valido
if 0 <= indice < len(lista):
    # Eliminamos el elemento en el indice especificado
    lista.pop(indice)
    # Mostramos la lista actualizada
    print("Lista actualizada:", lista)

# Actividad 11: Escribe un programa que permita al usuario ingresar una lista y un número, y cuente cuántas veces aparece ese número en la lista. 
# Pedimos al usuario que ingrese numeros separados por espacios
entrada = input("Ingrese numeros separados por espacios:")
# Convertimos los numeros en una lista de enteros
lista = list(map(int,entrada.split()))
# Pedimos al usuario que ingrese el numero a buscar
numero_a_buscar = int(input("Ingrese el numero que desea buscar:"))
# Contamos cuantas veces aparece el numero en la lista
cantidad = lista.count(numero_a_buscar)
# Mostramos la cantidad de veces que aparece el numero
print(f"El numero {numero_a_buscar} aparece {cantidad} veces en la lista.")

# Actividad 12: Escribe un programa que sume dos listas de números elemento por elemento. Las listas deben tener la misma longitud.
# Pedimos al usuario que ingrese la primera lista de numeros separados por espacios
entrada1 = input("Ingrese la primera lista de numeros separados por espacios:")
# Convertimos los numeros en una lista de enteros
lista1 = list(map(int,entrada1.split()))
# Pedimos al usuario que ingrese la segunda lista de numeros separados por espacios
entrada2 = input("Ingrese la segunda lista de numeros separados por espacios:")
# Convertimos los numeros en una lista de enteros
lista2 = list(map(int,entrada2.split()))
# Verificamos si las listas tienen la misma lingitud
if len(lista1) != len(lista2):
    print("Las listas deben tener la misma lengitud.")
else:
    # Sumamos las listas elemento por elemento
    suma_listas = [a + b for a, b in zip(lista1, lista2)]
    # Mostramos la lista resultante
    print("La suma de las listas es:", suma_listas)

# Actividad 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays 
# NumPy es una librería de Python utilizada para trabajar con datos numéricos, arrays y matrices.
# Permite realizar operaciones matemáticas sobre todos los elementos de un array de manera sencilla.
# También permite crear matrices de varias dimensiones, acceder a sus elementos y realizar operaciones como sumas, multiplicaciones y otros cálculos matemáticos.
import numpy as np
#arrays con numpy
numbers13=np.array([10,20,30,40])
print(numbers13)
result13=numbers13*2
print(result13)
#matrices con numpy
matriz13=np.array([
    [1,2,3],
    [4,5,6]
])
print(matriz13)
#acceso
print(matriz13[0][1])
#suma de matrices
matriz_b_13=np.array([
    [5,6,7],
    [7,8,9]
])
result13=matriz13+matriz_b_13
print(result13)