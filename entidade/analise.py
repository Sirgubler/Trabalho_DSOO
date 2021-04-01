from entidade.critico import Critico

class Analise:
    def __init__(self):
        self.__critico = None
        self.__comentario = None

    @property
    def critico(self):
        return self.__critico

    @critico.setter
    def critico(critico: Critico):
        self.__critico = critico

    @property
    def analise(self):
        return self.__comentario

    @analise.setter
    def analise(self, analise: str):
        self.__comentario = analise