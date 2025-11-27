import uuid
from datetime import datetime

class Pedido:
    def __init__(self, cliente, productos_cantidades: list):
        self.id = uuid.uuid4()
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos_cantidades = productos_cantidades

    def total(self) -> float:
        return sum(prod.precio * cantidad for prod, cantidad in self.productos_cantidades)

    def __str__(self):
        return f"Pedido de {self.cliente.nombre}, Total: {self.total():.2f}€"
