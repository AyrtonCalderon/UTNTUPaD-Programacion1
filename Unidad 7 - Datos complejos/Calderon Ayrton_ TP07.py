# Práctico 6: Estructuras de datos complejas

# ==========================================
# VALIDACIONES (arriba de todo el script)
# ==========================================

def pedir_telefono(mensaje):
    while True:
        tel = input(mensaje).strip()
        # Permite números, espacios y el signo +
        if tel.replace(" ", "").replace("+", "").isdigit():
            return tel
        else:
            print("Error: El teléfono solo puede contener números.")

def pedir_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip()
        # Valida que no esté vacío y solo tenga letras y espacios
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("Error: El nombre solo puede contener letras.")

def pedir_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            # Verificamos que esté en el rango de 1 a 10
            if 1 <= nota <= 10:
                return nota
            else:
                print("Error: La nota debe estar entre 1 y 10.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# =================================================================================================================
# 1) Añadimos frutas con sus respectivos precios
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# =================================================================================================================
# 2) Actualizar precios de productos
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# =================================================================================================================
# 3) Crear una lista que contenga únicamente las frutas sin los precios.
nombre_de_fruta = list(precios_frutas.keys())

# =================================================================================================================
# 4) Escribí un programa que permita almacenar y consultar números telefónicos
usuario = {}

for i in range(5):
    nombre = pedir_nombre("Ingrese un nuevo nombre de usuario: ")
    telefono = pedir_telefono("Ingrese el número de teléfono: ")
    usuario[nombre] = telefono

busqueda = pedir_nombre("Ingrese el nombre del usuario a buscar: ")

if busqueda in usuario:
    print("Teléfono:", usuario[busqueda])
else:
    print("El usuario no existe")

# =================================================================================================================
# 5) Solicita al usuario una frase e imprime palabras únicas y recuento
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras_unicas:
    recuento[palabra] = palabras.count(palabra)

print("Palabras unicas:", palabras_unicas)
print("Recuento: ", recuento)

# =================================================================================================================
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
alumnos = {}

for i in range(3):
    nombre_alumno = pedir_nombre("Ingrese el nombre del alumno: ")

    nota_1 = pedir_nota("Ingrese la primera nota: ")
    nota_2 = pedir_nota("Ingrese la segunda nota: ")
    nota_3 = pedir_nota("Ingrese la tercera nota: ")

    notas = (nota_1, nota_2, nota_3)
    alumnos[nombre_alumno] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / 3
    print("El promedio de", alumno, "es:", promedio)

# =======================================================================================
# 7) Sets con nombres de estudiantes
parcial_1 = {"Ana", "Juan", "Pedro", "María"}
parcial_2 = {"Pedro", "María", "Lucas", "Sofia"}

# Aprobaron ambos parciales (Intersección: Pedro y María)
aprobaron_ambos = parcial_1 & parcial_2
print("Aprobaron ambos parciales:", aprobaron_ambos)

# Aprobaron solo uno de los dos (Diferencia simétrica: Ana, Juan, Lucas y Sofia)
solo_uno = parcial_1 ^ parcial_2
print("Aprobaron solo uno de los dos:", solo_uno)

# Total de estudiantes que aprobaron al menos uno (Unión de todos)
total = parcial_1 | parcial_2
print("Total de estudiantes que aprobaron al menos un parcial:", total)

# =======================================================================================
# 8) Control de inventario
producto = pedir_nombre("Ingrese el nombre del producto: ")
inventario = {"mandarinas": 10, "naranjas": 5}

# Convertimos a minúsculas para buscar sin problemas de mayúsculas
producto_clave = producto.lower()

if producto_clave in inventario:
    print("Stock actual:", inventario[producto_clave])
    while True:
        try:
            unidades = int(input("¿Cuántas unidades querés agregar?: "))
            inventario[producto_clave] += unidades
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
else:
    while True:
        try:
            cantidad = int(input("Nuevo producto, ingrese stock inicial: "))
            inventario[producto_clave] = cantidad
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

# =======================================================================================
# 9) Agenda con claves tipo tupla
agenda = {
    ("Lunes", "10:00"): "Desayuno",
    ("Martes", "11:00"): "Clases de matematica",
    ("Miercoles", "19:00"): "Clase de ingles"
}

dia = input("Ingrese el dia: ")
hora = input("Ingrese la hora: ")

if (dia, hora) in agenda:
    print("Actividad:", agenda[(dia, hora)])
else:
    print("No hay ninguna actividad programada para ese dia y hora.")

# =======================================================================================
# 10) Inversión de diccionario
original = {"Argentina": "Buenos aires", "Chile": "Santiago"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario invertido:", invertido)

