from typing import List
from componente_cpu import ComponenteCPU

class computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componentes: List[ComponenteCPU] = []

    def agregar_componente(self, Componente: ComponenteCPU):
        self.componentes.append(self.componente)

    def calcular_costo(self) -> float:
        total = 0.0
        for comp in self.componentes:
            total += comp.calcular_subtotal()
            return total

    def calcular_precio_venta(self) -> float:
        costo = self.calcular_costo()
        # Si el costo es menor o igual a 50000 se le suma el 40%, sino el 30%
        if costo <= 50000:
            return costo * 1.40
        else:
            return costo * 1.30

    def mostrar_informacion(self):
        print(f"\n----- INFORMACIÓN DE LA COMPUTADORA -----")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("Componentes:")
        if not self.componentes:
            print("  No hay componentes cargados.")
        else:
            for comp in self.componentes:
                print(f"    {comp}")

        costo = self.calcular_costo()
        precio_venta = self.calcular_precio_venta()
        print(f"\nCosto total de la computadora: ${costo:.2f}")
        print(f"Precio de venta sugerido: ${precio_venta:.2f}")
        print("--------------------------------------------")