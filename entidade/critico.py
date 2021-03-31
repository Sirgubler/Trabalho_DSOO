from entidade.usuario import Usuario

class Critico(Usuario):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.livros_lidos = {}

    def adicionar_livro(self, livro: str, analise: str):
        self.livros_lidos[livro] = analise