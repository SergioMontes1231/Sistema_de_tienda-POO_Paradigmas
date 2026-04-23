from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, codigo_de_barras, nombre, categoria, precio_de_compra, precio_de_venta, stock):
        self.__codigo_de_barras = codigo_de_barras
        self._nombre = nombre
        self._categoria = categoria
        self.__precio_de_compra = precio_de_compra
        self.__precio_de_venta = precio_de_venta
        self.__stock = stock
        self.observaciones = []

    def codigo_de_barras(self):
        return self.__codigo_de_barras
    
    def nombre(self):
        return self._nombre
    
    def categoria(self):
        return self._categoria
    
    def Precio_de_compra(self):
        return self.__precio_de_compra
    
    def Precio_de_venta(self):
        return self.__precio_de_venta
    
    def stock(self):
        return self.__stock
    
    def set_stock(self, stock):
        self.__stock = stock
        self.notificar.observaciones()
    
    def vender(self, cantidad):
        from utils.SinStockException import SinstockException
        if cantidad > self.__stock:
            raise SinstockException(self._nombre, cantidad, self.__stock)
        
        self.__stock -= cantidad
        self.notificar.observaciones()
    
    def reponer_stock(self, cantidad):
        self.__stock += cantidad
        self.notificar.observaciones()
    
    @abstractmethod
    def calcular_impuesto(self):
        pass
    
    def precio_final(self):
        impuesto = self.calcular_impuesto()
        return self.__precio_de_venta + impuesto

    def agregar_observacion(self, observacion):
        self.observaciones.append(observacion)
        
    def remover_observacion(self, observacion):
        self.observaciones.remove(observacion)
        
    def notificar_observaciones(self):
        for observacion in self.observaciones:
            print(f"Observación para {self._nombre}: {observacion}")
            
    def  informacion(self):
        print(f"{self._nombre} ({self._categoria}) - Precio: ${self.__precio_de_venta}, Stock: {self.__stock}")
