from model.Venta import Venta


class Inventario:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ventas = []
        self.folio_actual = 1
        
    def agregar_producto(self, producto):
        self.productos[producto.codigo_barras] = producto
        
    def buscar_producto(self, codigo_barras):
        return self.productos.get(codigo_barras)
    
    def listar_productos(self, categoria, nombre):
        resultado = list(self.productos.values())
        
        if categoria:
            resultado = [p for p in resultado if p.categoria.lower() == categoria.lower()]
            
        if nombre:
            resultado = [p for p in resultado if nombre.lower() in p.nombre.lower()]
            
        return resultado
    
    def actualizar_stock(self, codigo_barras, nueva_cantidad):
        producto = self.buscar_producto(codigo_barras)
        if producto:
            producto.stock = nueva_cantidad
            return True
        return False
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        
    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None
    
    def registrar_venta(self, cliente):
        venta = Venta(self.folio_actual, cliente)
        self.ventas.append(venta)
        self.folio_actual += 1
        
    def obtener_folio(self):
        return self.folio_actual
    
    def listar_ventas(self):
        return self.ventas.copy()
        
        
