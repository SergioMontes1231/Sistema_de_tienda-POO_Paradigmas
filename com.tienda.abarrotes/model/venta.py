from datetime import datetime

class Venta:
    def __init___(self,folio,  cliente):
        self.folio = folio
        self.cliente = cliente
        self.detalles = []
        self.fecha = datetime.now()
        self.estrategia_descuento = None
        
    def folio(self):
        return self.folio
    
    def agregar_producto(self, producto, cantidad):
        from model.DetalleVenta import DetalleVenta
        detalle = DetalleVenta(producto, cantidad)
        self.detalles.append(detalle)
        producto.vender(cantidad)
        
    def estrategia_descuento(self, estrategia):
        self.estrategia_descuento = estrategia
        
    def subtotal(self):
        total = 0
        for detalles in self.detalles:
            total = total + detalles.subtotal()
        return total
    
    def descuento(self):
        if self.estrategia_descuento:
            self.estrategia_descuento.aplicar_descuento(self.subtotal())
            
    def total(self):
        self.subtotal = self.subtotal()
        self.descuento = self.descuento()
        return self.subtotal - self.descuento
    
    def finalizar_venta(self):
        if self.cliente:
            puntos = int(self.total() / 10)
            self.cliente.acumular_puntos(puntos)
        return self
    
    def detalles(self):
        return self.detalles.copy()
    
    def informacion(self):
        
       cliente = self.cliente.nombre if self.cliente else "Cliente general"
       encabezado = f"Folio: {self.folio} - Cliente: {cliente} - Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
       
       separador = "==========================00"
       
       detalles = "\n".join(str(d) for d in self.detalles)
       
       subtotal = f"Subtotal: ${self.subtotal():.2f}"
       descuento = f"Descuento: ${self.descuento():.2f}"
       total = f"Total: ${self.total():.2f}" 
       
       print(f"{encabezado}\n{separador}\n{detalles}\n{separador}\n{subtotal}\n{descuento}\n{total}")
