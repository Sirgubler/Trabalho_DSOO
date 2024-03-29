from entidade.usuario import Usuario

class Leitor(Usuario):
    def __init__(self, nome: str, senha: str, codigo: int):
        super().__init__(nome, senha, codigo)
        self.livros_lidos = {}

    def adicionar_livro(self, livro: str, nota: int):
        self.livros_lidos[livro] = nota