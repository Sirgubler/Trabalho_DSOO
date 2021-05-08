from persistencia.dao import DAO
from entidade.leitor import Leitor

class LeitorDAO(DAO):
    def __init__(self):
        super().__init__('leitores.pkl')

    def add(self, leitor: Leitor):
        if (leitor is not None) and (isinstance(leitor, Leitor)) and (isinstance(leitor.codigo, int)):
            super().add(leitor.codigo, leitor)
        
    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if isinstance(codigo, int):
            return super().remove(codigo)
