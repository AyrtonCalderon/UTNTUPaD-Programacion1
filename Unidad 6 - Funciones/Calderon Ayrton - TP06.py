#Ejercicio 1
#Definición de la funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa principal (Llamada a la funcion)
imprimir_hola_mundo()
#=============================================
#Ejercicio 2
#Definimos la función que recibe el nombre y DEVUELVE el saludo
def saludar_usuario(nombre):
    return(f"Saludos {nombre}")

#Programa principal
nombre_ingresado = input("Ingrese un nombre: ")

#Llamamos a la funcion y guardamos o imprimimos su resultado
saludo = saludar_usuario(nombre_ingresado)
print(saludo)

#================================================================================

#Ejercicio 3 
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa principal
nombre_ingresado = input("Ingrese un nombre: ")
apellido_ingresado = input("Ingrese un apellido: ")
edad_ingresada = input("Ingrese su edad: ")
residencia_ingresada = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre_ingresado,apellido_ingresado,edad_ingresada,residencia_ingresada)
#=================================================================================================
#Ejercicio 4

def calcular_area_circulo(radio):
    return 3.1416 * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio

#Programa principal
radio_ingresado = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio_ingresado)
perimetro = calcular_perimetro_circulo(radio_ingresado)

print(f"El area del circulo es {area}")
print(f"El perimetro es: {perimetro}")

#=========================================================================
#Ejercicio 5

def segundos_a_horas(segundos):
    return (segundos/3600)

segundos_ingresados = float(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos_ingresados)

print(f"El tiempo es: {horas}")

#================================================================================
#Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1,11):
        multiplicacion = numero*i
        print(f"{numero} X {i}= {multiplicacion}")

#Programa principal
numero=int(input("Ingrese un numero del 1 al 10 para ver su tabla de multiplicar: "))

tabla_multiplicar(numero)

#=========================================================================================
#Ejercicio 7

def operaciones_basicas(a, b):
    return ((a + b) , (a*b) , (a-b) , (a/b))

valor_a = float(input("Ingrese un numero: "))
valor_b = float(input("Ingree un numero: "))

#Programa principal
suma, multiplicacion, resta, division = operaciones_basicas(valor_a,valor_b)

#Imprimir por pantalla 
print(f"El valor de suma es: {suma}")
print(f"El valor de la multiplicacion es: {multiplicacion}")
print(f"El valor de la resta es: {resta}")
print(f"El valor de la division es: {division}")

#====================================================================================
#Ejercicio 8
def calcular_imc(peso,altura):
    return peso / (altura**2)

peso_usuario = float(input("Ingrese el peso: "))
altura_usuario = float(input("Ingrese la altura: "))

#Programa principal

resultado_IMC = calcular_imc(peso_usuario,altura_usuario)

print(f"Tu Índice de Masa Corporal (IMC) es: {resultado_IMC:.2f}")

#=======================================================================
#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return ((celsius*1.8)+32)

celsius_usuario = float(input("Ingrese los grados celsius: "))

#Programa principal

resultado_fahrenheit = celsius_a_fahrenheit(celsius_usuario)

print(f"Los grados en celsius son {celsius_usuario} y su conversion a fahrenheit son {resultado_fahrenheit}")

#====================================================================================================================
#Ejercicio 10

def calcular_promedio(a, b, c):
    return ((a + b + c)/3)

nota_1 = float(input("Ingrese la primer nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercer nota: "))

#Programa principal
resultado = calcular_promedio(nota_1, nota_2, nota_3)
print(f"El promedio de las 3 notas ingresadas es de: {resultado:.2f}")
