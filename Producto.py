class Producto:
    productos = {}  # Diccionario para almacenar los productos

    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta, callback=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta

        if callback is not None:
            self.precio_de_venta = callback(costo, margen_de_venta)
        else:
            self.precio_de_venta = costo / (1 - margen_de_venta)

        Producto.productos[id] = self

    @staticmethod
    def calcular_precio_venta(costo, margen_de_venta):
        return costo / (1 - margen_de_venta)

    @classmethod
    def registrar_producto(cls):
        id = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        costo = float(input("Ingrese el costo del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        margen_de_venta = float(input("Ingrese el margen de venta (porcentaje): ")) / 100

        Producto(id, nombre, descripcion, costo, cantidad, margen_de_venta, Producto.calcular_precio_venta)

    @classmethod
    def imprimir_productos(cls):
        for id, producto in cls.productos.items():
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, "
                  f"Costo: {producto.costo}, Cantidad: {producto.cantidad}, Precio de Venta: {producto.precio_de_venta}")


