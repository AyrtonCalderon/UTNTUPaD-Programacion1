from componente_cpu import ComponenteCPU
from computadora import computadora

def main():
    continuar = "SI"
    while continuar == "SI":
        print("\n------ NUEVA COTIZACION DE COMPUTADORA -----")
        marca = input("Ingrese la marca de la computadora: ")
        modelo = input("Ingrese el modelo de la computadora: ")

        pc = computadora(marca, modelo)

        while True:
            print("\n--- Carga de Componente ---")
            nombre_comp = input("Ingrese el nombre del componente (ej. Memoria RAM 2 Gb): ")
            marca_comp = input("Ingrese la marca del componente: ")
            
            # Validaciones básicas para evitar errores de tipeo en números
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad: "))
                    break
                except ValueError:
                    print("Error: Ingrese un numero entero válido.")

            while True:
                try:
                    precio = float(input("Ingrese el precio: "))
                    break
                except ValueError:
                    print("Error: Ingrese un numero valido para el precio.")

            componente = ComponenteCPU(nombre_comp, marca_comp, cantidad, precio)
            pc.agregar_componente(componente)

            resp_comp = input("Desea agregar otro componente a esta computadora? (SI/NO): ").strip().upper()
            if resp_comp != "SI":
                break

        # Mostrar resultados y cálculos
        pc.mostrar_informacion()

        # Preguntar si desea cotizar otra computadora
        continuar = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ").strip().upper()

    print("\n¡Programa finalizado!")

if __name__ == "__main__":
    main()