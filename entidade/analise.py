class Analise:

    def __init__(self, usuario, livro):
        self.__usuario = usuario
        self.__livro = livro
        self.__nota = None
        self.__critica = None
        self.__comentario = None
    
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def livro(self):
        return self.__livro

    @livro.setter
    def livro(self, livro):
        self.__livro = livro

    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nota: int):
        self.__nota = nota

    @property
    def critica(self):
        return self.__critica

    @critica.setter
    def critica(self, critica: str):
        self.__critica = critica

    @property
    def comentario(self):
        return self.__comentario

    @comentario.setter
    def comentario(self, comentario):
        self.__comentario = comentario