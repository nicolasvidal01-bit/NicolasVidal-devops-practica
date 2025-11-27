from services.TiendaService import TiendaService
from models.Usuario import Cliente, Administrador
from models.Producto import ProductoElectronico, ProductoRopa, Producto

def main():
    service = TiendaService()

    # Creando usuarios según práctica 1.2 (POO y herencia)
    c1 = Cliente("Javi", "javi@gmail.com", "Calle 1")
    c2 = Cliente("Juan", "juan@gmail.com", "Calle 2")
    c3 = Cliente("Luis", "luis@gmail.com", "Calle 3")
    admin = Administrador("Admin", "admin@gmail.com")
    for u in [c1, c2, c3, admin]:
        service.registrar_usuario(u)

    # Creando productos (uso de clases y herencia práctica 1.2)
    p1 = ProductoElectronico("Portátil", 899.99, 10, 24)
    p2 = ProductoRopa("Camiseta", 15.99, 50, "M", "azul")
    p3 = ProductoRopa("Pantalón", 39.99, 30, "L", "negro")
    p4 = ProductoElectronico("Auriculares", 49.99, 25, 12)
    p5 = Producto("Libro", 19.99, 70)
    for p in [p1, p2, p3, p4, p5]:
        service.añadir_producto(p)

    # Mostrar inventario (manejo de listas y métodos, práctica 1.1 y 1.2)
    print("Inventario inicial:")
    service.listar_productos()

    # Realizar pedidos (funciones y métodos, manejo de listas)
    pedido1 = service.realizar_pedido(c1.id, [(p1.id, 1), (p2.id, 2)])
    pedido2 = service.realizar_pedido(c2.id, [(p3.id, 3)])
    pedido3 = service.realizar_pedido(c3.id, [(p4.id, 1), (p5.id, 1)])

    # Mostrar resumen de pedidos (listas y loops, práctico 1.1)
    print("\nResumen de pedidos:")
    for pedido in [pedido1, pedido2, pedido3]:
        if pedido:
            print(pedido)

    # Mostrar pedidos específicos (filtrado con bucle, condicionales)
    print("\nPedidos de Javi:")
    for p in service.pedidos_por_usuario(c1.id):
        print(p)

    # Inventario actualizado (manipulación de listas)
    print("\nInventario actualizado:")
    service.listar_productos()

if __name__ == '__main__':
    main()
