from model.Producto import Producto

class ProductoUnitario(Producto):
    def __init__(self, codigo_barras, nombre, categoria, precio_compra, precio_venta, stock):
        super().__init__(codigo_barras, nombre, categoria, precio_compra, precio_venta, stock)
    
    def calcular_impuesto(self):
        categoria = self.get_categoria()
        if categoria == "Bebidas":
            return self.get_precio_venta() * 0.24 

        return self.get_precio_venta() * 0.16
