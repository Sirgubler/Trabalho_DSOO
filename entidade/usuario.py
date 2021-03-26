from abc import ABC, abstractclassmethod

class Usuario(ABC):

    @abstractclassmethod
    def __init__(self, nome):
        self.__nome = nome

    @property
    @abstractclassmethod
    def nome(self):
        pass

    @nome.setter
    @abstractclassmethod
    def nome(self, nome):
        pass
