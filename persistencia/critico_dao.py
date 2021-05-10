from persistencia.dao import DAO
from entidade.critico import Critico

class CriticoDAO(DAO):
    def __init__(self):
        super().__init__('persistencia//criticos.pkl')

    def add(self, critico: Critico):
        if (critico is not None) and (isinstance(critico, Critico)) and (isinstance(critico.codigo, int)):
            super().add(critico.codigo, critico)
        
    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if isinstance(codigo, int):
            return super().remove(codigo)
