from abc import ABC, abstractmethod

class Usuario(ABC):

    @abstractmethod
    def __init__(self, nome: str, senha: str):
        self.__nome = nome
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha
        