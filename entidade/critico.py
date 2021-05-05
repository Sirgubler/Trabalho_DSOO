from entidade.usuario import Usuario
from entidade.analise import Analise

class Critico(Usuario):
    def __init__(self, nome: str, senha: str):
        super().__init__(nome, senha)
        self.livros_analisados = {}
        self.analises = []

    def analisar_livro(self, livro: str, texto: str):
        analise = Analise(livro, texto)
        self.analises.append(analise)
        self.livros_analisados[analise.livro] = analise.texto
