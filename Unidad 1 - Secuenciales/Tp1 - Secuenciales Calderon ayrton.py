# Trabajo Practico Unidad 1
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizarla impresión por pantalla.

#   Ingreso de datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
Lugar_residencia = input("Ingrese su residencia: ")
#   Salida
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {Lugar_residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área ysu perímetro.

#CIRCULO
import math
#Radio
radio =float(input("Ingrese el radio de un circulo:"))

#area
area=float( math.pi*(radio**2))
print(f"Area: {area}")

#Perimetro
perimetro=float(2*math.pi*radio)
print(f"El perimetro es: {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese la cantidad en segundos: "))

horas = segundos / 3600

print("Es igual a ", horas, "horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = int(input("Ingrese un número: "))

print(num * 1)
print(num * 2)
print(num * 3)
print(num * 4)
print(num * 5)
print(num * 6)
print(num * 7)
print(num * 8)
print(num * 9)
print(num * 10)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

suma = numero_1+numero_2
division = numero_1/numero_2
multiplicacion = numero_1*numero_2
resta = numero_1-numero_2

print(f"Suma: {suma}")
print(f"Division: {division}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Resta: {resta}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso/(altura ** 2)

print(f"Su índice de masa corporal es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num_1 = float(input("Ingrese el primer numero: "))
num_2 = float(input("Ingrese el segundo numero: "))
num_3 = float(input("Ingrese el tercer numero: "))

promedio = (num_1 + num_2 + num_3) / 3

print(f"El promedio es: {promedio}")