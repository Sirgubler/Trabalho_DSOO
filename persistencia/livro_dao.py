from persistencia.dao import DAO
from entidade.livro import Livro

class LivroDAO(DAO):
    def __init__(self):
        super().__init__('persistencia//livros.pkl')

    def add(self, livro: Livro):
        if (livro is not None) and (isinstance(livro, Livro)) and (isinstance(livro.titulo, str)):
            super().add(livro.titulo, livro)
        
    def get(self, titulo: str):
        if isinstance(titulo, str):
            return super().get(titulo)

    def remove(self, titulo: str):
        if isinstance(titulo, str):
            return super().remove(titulo)