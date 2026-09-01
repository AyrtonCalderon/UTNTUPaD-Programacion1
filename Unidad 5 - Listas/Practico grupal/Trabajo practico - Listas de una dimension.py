#Ejercicio 4
# Pedir ingreso de datos
entrada = input("Ingrese numeros enteros separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

# Contar pares e impares
pares = sum(1 for x in numeros if x % 2 == 0)
impares = len(numeros) - pares

# Mostrar resultados
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)

#=====================================================
#Ejercicio 5
# Pedir lista de numeros y factor de multiplicacion
entrada = input("Ingrese numeros separados por espacios: ")
numeros = [float(x) for x in entrada.split()]
factor = float(input("Ingrese el numero por el cual desea multiplicar: "))

# Multiplicar cada elemento
resultado = [x * factor for x in numeros]

# Mostrar resultado
print("Lista multiplicada:", resultado)

#==================================
#Ejercicio 6

# Pedir ingreso de datos
entrada = input("Ingrese numeros separados por espacios: ")

lista_original = []
for x in entrada.split():
    lista_original.append(float(x))

# Guardamos directamente en el set
sin_duplicados = set(lista_original)

print("Elementos sin duplicados:", sin_duplicados)
