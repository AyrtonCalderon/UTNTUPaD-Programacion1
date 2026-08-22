#Trabajo practico N°3 - Condicionales
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

Edad= int(input("Ingrese la edad del usuario: "))

#Condicional
if Edad >= 18:
    print("Es mayor de edad")
elif Edad < 18 :
    print("No es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

Nota=int(input("Ingrese la nota del alumno: "))

if Nota>=6:
    print("Aprobado")
elif Nota <=6:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.


numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Pertenece a la categoria: Niño")
elif edad < 18:
    print("Pertenece a la categoria: Adolescente")
elif edad < 30:
    print("Pertenece a la categoria: Adulto joven")
else:
    print("Pertenece a la categoria: Adulto")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.


contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Contraseña incorrecta")
else:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3] mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete:
#https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and (mediana > moda):
    print("Resultado: Sesgo positivo")
elif media < mediana and (mediana < moda):
    print("Resultado: Sesgo negativo")
elif (media == mediana == moda):
    print("Resultado: Sin sesgo")
else:
    print("Resultado: No cumple exactamente con ninguno de los tres criterios teoricos de sesgo estricto.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

texto = input("Ingrese una frase o palabra: ")

vocales = "aeiouáéíóú"

if texto and texto[-1].lower() in vocales:
    texto += "!"

print("Resultado:", texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solicitamos el nombre y la opción deseada
nombre = input("Ingrese su nombre: ")
opcion = input("Elija una opción (1: MAYUSCULAS, 2: minusculas, 3: Primera Mayuscula): ")

# Transformamos segun la opción seleccionada
if opcion == "1":
    resultado = nombre.upper()
    print("Resultado:", resultado)
elif opcion == "2":
    resultado = nombre.lower()
    print("Resultado:", resultado)
elif opcion == "3":
    resultado = nombre.title()
    print("Resultado:", resultado)
else:
    print("Opcion inválida. Por favor, elija 1, 2 o 3.")

## Solicitamos la magnitud del terremoto (usamos float para permitir decimales)
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Evaluamos la categoría según la escala de Richter
if magnitud < 3:
    print("Categoria: Muy leve (imperceptible)")
elif magnitud < 4:
    print("Categoria: Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Categoria: Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Categoria: Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Categoria: Muy Fuerte (puede causar daños significativos)")
else:
    print("Categoria: Extremo (puede causar graves daños a gran escala)")

#9Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla

## Solicitamos los datos al usuario
hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

# Convertimos la fecha a una clave numérica (MMDD) para comparar fácilmente
# Ejemplo: 21 de Diciembre -> 1221, 20 de Marzo -> 320 
fecha = mes * 100 + dia

# Determinamos el periodo base
if 321 <= fecha <= 620:
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif 621 <= fecha <= 920:
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif 921 <= fecha <= 1220:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:  # Desde el 21 de diciembre hasta el 20 de marzo
    estacion_norte = "Invierno"
    estacion_sur = "Verano"

# Imprimimos la estacion segun el hemisferio
if hemisferio == "N":
    print("Se encuentra en:", estacion_norte)
elif hemisferio == "S":
    print("Se encuentra en:", estacion_sur)
else:
    print("Hemisferio no válido. Por favor ingrese 'N' o 'S'.")