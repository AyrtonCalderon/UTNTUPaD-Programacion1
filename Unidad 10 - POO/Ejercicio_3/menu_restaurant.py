from ingrediente import Ingrediente
from plato import Plato

# ==========================================
# FUNCIONES DE VALIDACIÓN
# ==========================================
def pedir_texto(mensaje: str) -> str:
    """Pide un texto y valida que solo contenga letras y espacios."""
    while True:
        entrada = input(mensaje).strip()
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
    """Obliga al usuario a responder 'S' o 'N'."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ["s", "n"]:
            return respuesta == "s"
        print(" Error: Debe responder únicamente con 'S' o 'N'. Intente de nuevo.\n")


# ==========================================
# CÓDIGO PRINCIPAL - CARGA DE DATOS
# ==========================================
platosMenu = []

while True:
    nombreCompleto = pedir_texto("Nombre del plato o bebida: ")
    precio = pedir_numero_positivo("Precio: ")

    # Preguntamos si es bebida
    esBebida = pedir_confirmacion("Es bebida? (S/N): ")

    nuevo_plato = Plato(nombreCompleto, precio, esBebida)

    # Si no es bebida obligamos a ingresar al menos 1 ingrediente
    if not esBebida:
        agregar_mas = True
        while agregar_mas:
            nombre_ingrediente = pedir_texto("Nombre del ingrediente: ")
            cantidad = pedir_numero_positivo("Cantidad: ")
            unidad = pedir_texto("Unidad de medida: ")

            nuevo_ing = Ingrediente(nombre_ingrediente, cantidad, unidad)
            nuevo_plato.agregarIngrediente(nuevo_ing)

            agregar_mas = pedir_confirmacion("Agregar otro ingrediente a este plato? (S/N): ")

    platosMenu.append(nuevo_plato)

    continuar = pedir_confirmacion("\nDesea agregar otro plato (S/N): ")
    if not continuar:
        break


# ==========================================
# IMPRESIÓN CON EL FORMATO SOLICITADO
# ==========================================
print("\n-----------MENÚ----------------")
for p in platosMenu:
    print(p.nombreCompleto)
    
    # Formatea el precio sin decimales si es entero (ej: 450 en vez de 450.0)
    precio_str = f"{p.precio:.0f}" if p.precio.is_integer() else f"{p.precio}"
    print(f"Precio: $ {precio_str}")
    
    if not p.esBebida:
        print("Ingredientes:")
        print("Nombre\tCantidad\tUnidad de Medida")
        for ing in p.listadeIngredientes:
            cant_str = f"{ing.cantidad:.0f}" if isinstance(ing.cantidad, float) and ing.cantidad.is_integer() else f"{ing.cantidad}"
            print(f"{ing.nombre}\t{cant_str}\t{ing.unidad_medida}")
            
    print("----------------------------------")