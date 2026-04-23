class Cliente:
    def __init__(self, nombre, telefono, puntos=0):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__puntos = puntos
    
    def nombre(self):
        return self.__nombre
    
    def telefono(self):
        return self.__telefono
    
    def puntos(self):
        return self.__puntos
    
    def acumular_puntos(self, puntos):
        self.__puntos += puntos
    
    def redimir_puntos(self, puntos):
        if puntos <= self.__puntos:
            self.__puntos -= puntos
            return True
        return False
    
    def  informacion(self):
        print(f"{self.__nombre} - Tel: {self.__telefono} - Puntos: {self.__puntos}")
