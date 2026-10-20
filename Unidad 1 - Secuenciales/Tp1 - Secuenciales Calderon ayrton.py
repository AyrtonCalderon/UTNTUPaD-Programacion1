import math


# ==========================================
# FUNCIONES PARA VALIDAR LOS DATOS
# ==========================================

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        # Acepta letras, espacios, guiones y apostrofes.
        caracteres_validos = all(
            caracter.isalpha() or caracter.isspace()
            or caracter in "-'’"
            for caracter in texto
        )

        if texto and caracteres_validos and any(
            caracter.isalpha() for caracter in texto
        ):
            return texto

        print("Error: ingrese solamente letras.")


def pedir_entero(mensaje, minimo=None, distinto_de_cero=False):
    while True:
        try:
            numero = int(input(mensaje))

            if distinto_de_cero and numero == 0:
                print("Error: el numero no puede ser cero.")
            elif minimo is not None and numero < minimo:
                print(f"Error: el numero debe ser mayor o igual a {minimo}.")
            else:
                return numero

        except ValueError:
            print("Error: ingrese un numero entero valido.")


def pedir_decimal(mensaje, minimo=None):
    while True:
        try:
            numero = float(input(mensaje).replace(",", "."))

            if not math.isfinite(numero):
                print("Error: ingrese un numero finito.")
            elif minimo is not None and numero < minimo:
                print(f"Error: el valor debe ser mayor o igual a {minimo}.")
            else:
                return numero

        except ValueError:
            print("Error: ingrese un numero valido.")


# ==========================================
# 1) HOLA MUNDO
# ==========================================

print("Hola Mundo!")


# ==========================================
# 2) SALUDO CON EL NOMBRE
# ==========================================

nombre = pedir_texto("Ingrese su nombre: ")

print(f"Hola {nombre}!")


# ==========================================
# 3) DATOS PERSONALES
# ==========================================

nombre = pedir_texto("Ingrese su nombre: ")
apellido = pedir_texto("Ingrese su apellido: ")
edad = pedir_entero("Ingrese su edad: ", minimo=0)
lugar_residencia = pedir_texto("Ingrese su lugar de residencia: ")

print(
    f"Soy {nombre} {apellido}, tengo {edad} años "
    f"y vivo en {lugar_residencia}."
)


# ==========================================
# 4) AREA Y PERIMETRO DE UN CIRCULO
# ==========================================

radio = pedir_decimal("Ingrese el radio del circulo: ", minimo=0)

area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"Area: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}")


# ==========================================
# 5) CONVERTIR SEGUNDOS A HORAS
# ==========================================

segundos = pedir_entero(
    "Ingrese la cantidad de segundos: ",
    minimo=0
)

horas = segundos / 3600

print(f"Equivale a {horas:.2f} horas.")


# ==========================================
# 6) TABLA DE MULTIPLICAR
# ==========================================

numero = pedir_entero("Ingrese un numero entero: ")

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# ==========================================
# 7) OPERACIONES CON DOS NUMEROS ENTEROS
# ==========================================

numero_1 = pedir_entero(
    "Ingrese el primer numero entero: ",
    distinto_de_cero=True
)

numero_2 = pedir_entero(
    "Ingrese el segundo numero entero: ",
    distinto_de_cero=True
)

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division:.2f}")


# ==========================================
# 8) INDICE DE MASA CORPORAL (IMC)
# ==========================================

peso = pedir_decimal("Ingrese su peso en kg: ", minimo=0)

while peso == 0:
    print("Error: el peso debe ser mayor que cero.")
    peso = pedir_decimal("Ingrese su peso en kg: ", minimo=0)

altura = pedir_decimal("Ingrese su altura en metros: ", minimo=0)

while altura == 0:
    print("Error: la altura debe ser mayor que cero.")
    altura = pedir_decimal("Ingrese su altura en metros: ", minimo=0)

imc = peso / (altura**2)

print(f"Su indice de masa corporal es: {imc:.2f}")


# ==========================================
# 9) CELSIUS A FAHRENHEIT
# ==========================================

celsius = pedir_decimal("Ingrese la temperatura en grados Celsius: ")

fahrenheit = (9 / 5) * celsius + 32

print(f"Temperatura en Fahrenheit: {fahrenheit:.2f} grados.")


# ==========================================
# 10) PROMEDIO DE TRES NUMEROS
# ==========================================

num_1 = pedir_decimal("Ingrese el primer numero: ")
num_2 = pedir_decimal("Ingrese el segundo numero: ")
num_3 = pedir_decimal("Ingrese el tercer numero: ")

promedio = (num_1 + num_2 + num_3) / 3

print(f"El promedio es: {promedio:.2f}")