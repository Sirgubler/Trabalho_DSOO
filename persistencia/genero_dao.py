from persistencia.dao import DAO
from entidade.genero import Genero

class GeneroDAO(DAO):
    def __init__(self):
        super().__init__('persistencia//generos.pkl')

    def add(self, genero: Genero):
        if (genero is not None) and (isinstance(genero, Genero)) and (isinstance(genero.nome, str)):
            super().add(genero.nome, genero)
        
    def get(self, genero: str):
        if isinstance(genero, str):
            return super().get(genero)

    def remove(self, genero: str):
        if isinstance(genero, str):
            return super().remove(genero)