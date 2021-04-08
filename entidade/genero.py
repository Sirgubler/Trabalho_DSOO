class Genero:

    def __init__(self, estilo: str):
        self.__estilo = estilo

    @property
    def estilo(self):
        return self.__estilo

    @estilo.setter
    def estilo(self, estilo: str):
        self.__estilo = estilo