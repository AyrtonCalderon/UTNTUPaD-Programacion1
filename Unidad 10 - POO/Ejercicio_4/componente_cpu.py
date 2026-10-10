class ComponenteCPU:
    def __init__(self,componente: str, marca:str, cantidad: int, precio: float):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def calcular_subtotal(self) -> float:
        return self.cantidad * self.precio

    def __str__(self):
        return(
            f"- {self.componente} ({self.marca}) | Cantidad: {self.cantidad}"
            f"| Precio Unitario: ${self.precio: .2f} |  Subtotal: ${self.calcular_subtotal():.2f}"
        )