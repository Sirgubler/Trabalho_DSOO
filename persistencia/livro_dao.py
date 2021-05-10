from persistencia.dao import DAO
from entidade.livro import Livro

class LivroDAO(DAO):
    def __init__(self):
        super().__init__('persistencia//livros.pkl')

    def add(self, livro: Livro):
        if (livro is not None) and (isinstance(livro, Livro)) and (isinstance(livro.codigo, int)):
            super().add(livro.codigo, livro)
        
    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if isinstance(codigo, int):
            return super().remove(codigo)