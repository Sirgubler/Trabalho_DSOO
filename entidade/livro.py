from entidade.autor import Autor
from entidade.genero import Genero
from entidade.analise import Analise

class Livro:
    def __init__(self, nome: str, autor: Autor, genero: Genero):
        self.__nome = nome
        self.__autor = autor
        self.__genero = genero
        self.__notas_leitores = {}
        self.__media_notas = None
        self.__analises_criticos = {}
        self.__notas = {}

    def adicionar_avaliacao(self, leitor: str, nota: int):
        notas_dadas = self.__notas
        notas_dadas.update({leitor:nota}) 

    def adicionar_analise(self, critico: str, critica: str):
        analises = self.__analises_criticos
        analises.update({critico:critica})
    
    @property
    def analises_criticos(self):
        return self.__analises_criticos
    
    @property
    def nome(self):
        return

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 
        
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        self.__autor = autor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: Genero):
        self.__genero = genero