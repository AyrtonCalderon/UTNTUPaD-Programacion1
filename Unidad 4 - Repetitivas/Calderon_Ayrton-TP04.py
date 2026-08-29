#Practico 4 : Estructuras repetitivas

#Ejercicio 1
for n in range(101):
    print(n)

#Ejercicio 2

num=int(input("Ingrese un numero entero: "))

i=0
while num > 0:
    i = i+1
    num=num // 10

print("La cantidad de digitos es: ",i)

#Ejercicio 3 
num_1=int(input("Ingrese el primer numero: "))
num_2=int(input("Ingrese el segundo numero: "))

suma=0

for ite in range((num_1+1),num_2):
    suma += ite

print("La suma de los numeros intermedios es:", suma)

#Ejercicio 4

nu=int(input("Ingrese un numero: "))

su=0
while nu != 0:
    su += nu
    nu=int(input("Ingrese un nuevo numero: "))

print("El total acumulado es: ",su)

#Ejercicio 5

#Paso 1: Generar el número aleatorio
import random
num_secreto= random.randint(0,9)

#Paso 2: La estructura principal

n1=int(input("Ingrese un numero: "))

intentos=1

while n1 != num_secreto:
    intentos += 1
    n1 = int(input("Incorrecto. Intenta de nuevo: "))

print("Adivinaste El número era:", num_secreto)
print("Cantidad de intentos:", intentos)

#EJERCICIO 6 
for nume in range(100, -1, -2):
    print(nume)
    
#EJERCICIO 7
n_entero = int(input("Ingrese un numero: "))   

suma = 0  # La bolsa empieza vacía

for i in range(0, (n_entero + 1)):  # 'i' camina desde 0 hasta n_entero
    suma += i  # Metemos el valor de 'i' adentro de la bolsa 'suma'

print("La suma total es:", suma)

#EJERCICIO 8
pares=0
impares=0
positivos=0
negativos=0

cantidad=5

for i in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#Ejercicio 9

cantidad = 100
suma = 0

for i in range(cantidad):
    num = int(input("Ingrese un numero: "))
    suma += num

media = suma / cantidad

print("La media de los números es:", media)

#Ejercicio 10

numero = int(input("Ingrese un numero: "))
invertido = 0

while numero > 0:
    ultimo_digito = numero % 10          # Sacamos el último numero (ej: de 123 saca 3)
    invertido = (invertido * 10) + ultimo_digito  # Lo agregamos al nuevo numero
    numero = numero // 10                # Le sacamos el ultimo numero a 'numero' (queda 1)

print("El número invertido es:", invertido)






