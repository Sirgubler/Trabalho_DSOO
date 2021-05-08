from entidade.usuario import Usuario
from entidade.analise import Analise

class Critico(Usuario):
    def __init__(self, nome: str, senha: str, codigo: int):
        super().__init__(nome, senha, codigo)
        self.livros_analisados = {}
        self.analises = []

    def analisar_livro(self, livro, texto: str):
        analise = Analise(livro, texto)
        self.analises.append(analise)
        self.livros_analisados[analise.livro.titulo] = analise.texto
