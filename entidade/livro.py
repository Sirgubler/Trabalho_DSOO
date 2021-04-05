from entidade.autor import Autor
from entidade.genero import Genero

class Livro:
    def __init__(self, titulo: str, autor: str, genero: str):
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
    def autor(self, autor: str):
        return self.__autor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        return self.__genero