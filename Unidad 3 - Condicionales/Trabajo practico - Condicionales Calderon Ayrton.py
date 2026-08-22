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


contrasena = input("Ingrese una contraseña: ")

if 8 <= len(contrasena) <= 14:
    print("Contraseña incorrecta")
else:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")