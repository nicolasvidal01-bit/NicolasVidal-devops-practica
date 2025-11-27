from models.Usuario import Cliente, Administrador
from models.Producto import Producto
from models.Pedido import Pedido

class TiendaService:
    def __init__(self):
        self.usuarios = []
        self.productos = []
        self.pedidos = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def añadir_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.id != id]

    def listar_productos(self):
        for p in self.productos:
            print(p)

    def realizar_pedido(self, id_cliente, lista_prod_cant):
        cliente = next((u for u in self.usuarios if u.id == id_cliente and isinstance(u, Cliente)), None)
        if cliente is None:
            return None
        productos_cant = []
        for prod_id, cantidad in lista_prod_cant:
            producto = next((p for p in self.productos if p.id == prod_id), None)
            if not producto or not producto.hay_stock(cantidad):
                return None
            productos_cant.append((producto, cantidad))
        for producto, cantidad in productos_cant:
            producto.actualizar_stock(-cantidad)
        pedido = Pedido(cliente, productos_cant)
        self.pedidos.append(pedido)
        return pedido

    def pedidos_por_usuario(self, id_usuario):
        return sorted([p for p in self.pedidos if p.cliente.id == id_usuario], key=lambda x: x.fecha)
