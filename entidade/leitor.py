class Leitor:
    def __init__(self, nome: str):
        self.__nome = nome
        self.livros_lidos = {}

    @property
    def nome(self):
        return self.__nome

    def adicionar_livro(self, livro: str, nota: int):
        self.livros_lidos[livro] = nota