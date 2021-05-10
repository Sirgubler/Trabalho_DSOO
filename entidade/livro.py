from entidade.autor import Autor
from entidade.genero import Genero

class Livro:
    def __init__(self, titulo: str, autor: Autor, genero: Genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

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