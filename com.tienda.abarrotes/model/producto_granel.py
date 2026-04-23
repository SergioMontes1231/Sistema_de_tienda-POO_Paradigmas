import model.Producto as Producto

class ProductoGranel(Producto):
    def __init__(self, codigo_de_barras, nombre, categoria, precio_de_compra, precio_de_venta, stock, unidad_medida = "kg"):
        super().__init__(codigo_de_barras, nombre, categoria, precio_de_compra, precio_de_venta, stock)
        self._unidad = unidad_medida

    def calcular_impuesto(self):
        return self.Precio_de_venta() * 0.16
    
    def unidad_medida(self):
        return self._unidad
    
