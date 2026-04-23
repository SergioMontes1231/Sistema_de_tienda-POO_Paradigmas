class DetalleVenta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        
    def producto(self):
        return self.producto
    
    def cantidad(self):
        return self.cantidad
    
    def precio_unitario(self):
        return self.producto.precio_final()
    
    def subtotal(self):
        return self.precio_unitario() * self.cantidad
    
    def informacion(self):
        print(f"{self.producto.nombre()} x{self.cantidad} - Subtotal: ${self.subtotal():.2f}")
