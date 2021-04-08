from entidade.livro import Livro
from limite.tela_livro import TelaLivro
from controle.controlador_autor import ControladorAutor
from controle.controlador_genero import ControladorGenero

class ControladorLivro:

    def __init__(self, controlador_principal):
        self.__livros = []
        self.__tela_livro = TelaLivro()
        self.__controlador_autor = ControladorAutor(self)
        self.__controlador_genero = ControladorGenero(self)
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    def abrir_tela_livro(self):
        pass

    def fechar_tela(self):
        self.__manter_tela_aberta = False