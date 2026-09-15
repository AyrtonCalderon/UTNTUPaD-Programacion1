# PRACTICA GRUPAL - FUNCIONES

#Ejercicio A

# --- DATOS INICIALES ---
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de menta", 50],
    [4, "Huevos Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]  

empleados = {
    1100: "Jose Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gaston Garcia"
}

claves_Tecnico = ("admin", "CCCDDD", "2020")
golosinasPedidas = []


# FUNCIONES 

def pedir_golosina(golosinas, empleados, golosinasPedidas):
    legajo = int(input("Ingrese su legajo: "))

    if legajo not in empleados:
        print("Usted no es empleado")
        return

    print(f"Bienvenido {empleados[legajo]}")
    codigo_golosina = int(input("Ingrese el codigo de la golosina: "))

    for go in golosinas:
        if go[0] == codigo_golosina:
            if go[2] > 0:
                go[2] -= 1
                print(f"Disfrute su {go[1]}")

                # Registrar en el historial de pedidos
                pedida = False
                for pedido in golosinasPedidas:
                    if pedido[0] == go[0]:
                        pedido[2] += 1
                        pedida = True
                        break
                
                if not pedida:
                    golosinasPedidas.append([go[0], go[1], 1])
            else:
                print("Lo sentimos, no hay stock disponible de esta golosina.")
            return  # Salimos de la funcion al encontrar el producto

    print("Codigo de golosina no válido.")


def mostrar_golosinas(golosinas):
    print("\n   MENÚ DE GOLOSINAS    ")
    print("Codigo | Denominacion | Stock")
    for go in golosinas:
        print(f"{go[0]} | {go[1]} | {go[2]}")


def rellenar_golosinas(golosinas):
    codigo_golosina = int(input("Ingrese el codigo de la golosina: "))
    cantidad = int(input("Ingrese la cantidad a rellenar: "))

    for go in golosinas:
        if go[0] == codigo_golosina:
            go[2] += cantidad
            print("Stock actualizado con exito.")
            return

    print("Codigo de golosina no válido.")


# --- BUCLE PRINCIPAL ---

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("a. Pedir golosina")
    print("b. Mostrar golosinas")
    print("c. Rellenar golosinas")
    print("d. Apagar máquina")
    
    opcion = input("Seleccione una opcion: ").lower()

    if opcion == "a":
        pedir_golosina(golosinas, empleados, golosinasPedidas)
    elif opcion == "b":
        mostrar_golosinas(golosinas)
    elif opcion == "c":
        rellenar_golosinas(golosinas)
    elif opcion == "d":
        print("Apagando la maquina expendedora... ¡Hasta luego!")
        break
    else:
        print("Opcion no válida, intente nuevamente.")
