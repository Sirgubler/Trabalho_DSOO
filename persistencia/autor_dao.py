from persistencia.dao import DAO
from entidade.autor import Autor

class AutorDAO(DAO):
    def __init__(self):
        super().__init__('persistencia//autores.pkl')

    def add(self, autor: Autor):
        if (autor is not None) and (isinstance(autor, Autor)) and (isinstance(autor.nome, str)):
            super().add(autor.nome, autor)
        
    def get(self, nome: str):
        if isinstance(nome, str):
            return super().get(nome)

    def remove(self, nome: str):
        if isinstance(nome, str):
            return super().remove(nome)