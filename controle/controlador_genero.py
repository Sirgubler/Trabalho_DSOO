from entidade.genero import Genero
from limite.tela_genero import TelaGenero

class ControladorGenero:

    def __init__(self, controlador_livro):
        self.__generos = []
        self.__tela_genero = TelaGenero()
        self.__controlador_livro = controlador_livro
        self.__manter_tela_aberta = True

    def abrir_tela_genero(self):
        pass

    def fechar_tela(self):
        self.__manter_tela_aberta = False