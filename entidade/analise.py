class Analise():
    def __init__(self, livro: str, texto: str):
        self.__livro = livro
        self.__texto = texto

    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, texto):
        self.__texto = texto

    @property
    def livro(self):
        return self.__livro

    @livro.setter
    def livro(self, livro):
        self.__livro = livro