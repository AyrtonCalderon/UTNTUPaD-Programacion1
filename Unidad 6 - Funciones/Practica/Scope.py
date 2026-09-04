#Definicion de funcion
def factorial(num):
    global numero
    numero = 1
    print(f"El numero global es {numero}")
    for i in range(1,num+1) :
        numero *= i
    return numero

#Programa principal
numero = int(input("Ingrese un numero natural: ")) #Variable global
if numero >= 0:
    fact = factorial(numero)
    print("El factorial de", numero, "es", fact)
else:
    print("No existe el factorial de un numero negativo")

