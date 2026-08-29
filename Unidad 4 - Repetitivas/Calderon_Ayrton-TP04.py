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




