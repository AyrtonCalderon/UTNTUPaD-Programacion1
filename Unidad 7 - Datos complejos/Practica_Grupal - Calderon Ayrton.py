# PRACTICA GRUPAL - FUNCIONES
# Ejercicio 1

# Lista
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

# Diccionario
empleados = {
    1100: "Jose Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gaston Garcia"
}

# Tupla
claves_Tecnico = ("admin", "CCCDDD", "2020")

# Historial de pedidos
golosinasPedidas = []

# Bucle principal de la máquina
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("a. Pedir golosina")
    print("b. Mostrar golosinas")
    print("c. Rellenar golosinas")
    print("d. Apagar máquina")
    
    opcion = input("Seleccione una opción: ").lower()

    # A. Pedir golosina
    if opcion == "a":
        legajo = int(input("Ingrese su legajo: "))

        if legajo in empleados:
            print(f"Bienvenido {empleados[legajo]}")
            codigo_golosina = int(input("Ingrese el codigo de la golosina: "))
            encontrado = False

            for go in golosinas:
                if go[0] == codigo_golosina:
                    encontrado = True
                    if go[2] > 0:
                        go[2] -= 1
                        print(f"¡Disfrute su {go[1]}!")

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
                    break

            if not encontrado:
                print("Código de golosina no válido.")
        else:
            print("Usted no es empleado")

    # B. Mostrar golosinas
    elif opcion == "b":
        print("--- MENÚ DE GOLOSINAS ---")
        print("Codigo | Denominacion | Stock")
        for go in golosinas:
            print(f"{go[0]} | {go[1]} | {go[2]}")

    # C. Rellenar golosinas
    elif opcion == "c":
        codigo_golosina = int(input("Ingrese el codigo de la golosina: "))
        cantidad = int(input("Ingrese la cantidad a rellenar: "))
        encontrado = False

        for go in golosinas:
            if go[0] == codigo_golosina:
                go[2] += cantidad
                encontrado = True
                print("Stock actualizado con éxito.")
                break

        if not encontrado:
            print("Código de golosina no válido.")

    # D. Apagar máquina
    elif opcion == "d":
        print("Apagando la máquina expendedora... ¡Hasta luego!")
        break

    else:
        print("Opción no válida, intente nuevamente.")
