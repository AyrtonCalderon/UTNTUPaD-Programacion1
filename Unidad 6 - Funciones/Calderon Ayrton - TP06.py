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
