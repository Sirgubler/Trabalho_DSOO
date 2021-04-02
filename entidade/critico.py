from entidade.usuario import Usuario
from entidade.analise import Analise

class Critico(Usuario):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.livros_analisados = []

    def analisar_livro(self, livro: str, texto: str):
        analise = Analise(livro, texto)
        self.livros_analisados.append(analise)