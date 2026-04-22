from abc import ABC, abstractmethod
from typing_extensions import List

class Producto(ABC):
    def __init__(self, codigo_barras: int, nombre: str, categoria: List):
        pass