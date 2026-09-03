#Definicion de funciones 
def obtener_resto (num1,num2):
    return num1 - num2 * (num1 // num2) # % sirve para obtener el resto de divir num1 y num2


def es_multiplo (x,y):
    return obtener_resto(x,y) == 0
#Programa principal

a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))

resto= obtener_resto(a,b)
print(f"El resto entre {a} y {b} es {resto}")

if es_multiplo(a,b):
    print(f"{a} es multiplo de {b}")