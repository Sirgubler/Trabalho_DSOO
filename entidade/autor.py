from entidade.pessoa import Pessoa

class Autor(Pessoa):

    def __init__(self, nome: str):
        super().__init__(nome)
        self.__livros = []

    @property
    def livros(self):
        return self.__livros

    @livros.setter
    def livros(self, livros: list):
        self.__livros = livros

    def adicionar_livro(self, livro):
        self.__livros.append(livro)