from ingrediente import Ingrediente
from plato import Plato

# ==========================================
# FUNCIONES DE VALIDACIÓN (Ubicar acá arriba)
# ==========================================
def pedir_texto(mensaje: str) -> str:
    """Pide un texto y valida que solo contenga letras y espacios."""
    while True:
        entrada = input(mensaje).strip()
        # Permite espacios entre palabras (ej: "Sopa de letras") y valida solo letras
        if entrada and entrada.replace(" ", "").isalpha():
            return entrada
        print(" Error: Debe ingresar solo letras (sin números ni símbolos). Intente de nuevo.\n")

def pedir_numero_positivo(mensaje: str) -> float:
    """Pide un número y valida que sea float positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print(" Error: El número debe ser mayor a 0.\n")
        except ValueError:
            print(" Error: Debe ingresar un número válido (ej: 1500 o 1.5).\n")

def pedir_confirmacion(mensaje: str) -> bool:
    """Obliga al usuario a responder 's' o 'n'. Devuelve True si es 's'."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ["s", "n"]:
            return respuesta == "s"
        print(" Error: Debe responder únicamente con 'S' o 'N'. Intente de nuevo.\n")

platosMenu = []

#Bucle para cargar N platos
# Bucle para cargar N platos
while True:
    # 1. Cambiá input(...) por pedir_texto(...)
    nombreCompleto = pedir_texto("Nombre del plato o bebida: ")
    
    # 2. Cambiá float(input(...)) por pedir_numero_positivo(...)
    precio = pedir_numero_positivo("Precio: ")

    resp = input("Es bebida? (S/N): ").strip().lower()
    esBebida = (resp == "s")

    nuevo_plato = Plato(nombreCompleto, precio, esBebida)

    if not esBebida:
        agregar_mas = "s"
        while agregar_mas == "s":
            # 3. Aplicá pedir_texto y pedir_numero_positivo a los ingredientes
            nombre_ingrediente = pedir_texto("Nombre del ingrediente: ")
            cantidad = pedir_numero_positivo("Cantidad: ")
            unidad = pedir_texto("Unidad de medida: ")

            nuevo_ing = Ingrediente(nombre_ingrediente, cantidad, unidad)
            nuevo_plato.agregarIngrediente(nuevo_ing)

            agregar_mas = input("Agregar otro ingrediente a este plato? (S/N): ").strip().lower()

    platosMenu.append(nuevo_plato)

    continuar = input("\nDesea agregar otro plato (S/N): ").strip().lower()
    if continuar != "s":
        break