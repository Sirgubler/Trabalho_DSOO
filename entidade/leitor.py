from entidade.usuario import Usuario

class Leitor(Usuario):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.livros_lidos = {}

    @property
    def livros_lidos(self):
        return self.livros_lidos
        
    def adicionar_livro(self, livro: str, nota: int):
        self.livros_lidos[livro] = nota