from entidade.autor import Autor
from limite.tela_autor import TelaAutor

class ControladorAutor:

    def __init__(self, controlador_livro):
        self.__autores = []
        self.__tela_autor = TelaAutor()
        self.__controlador_livro = controlador_livro
        self.__manter_tela_aberta = True

    def abrir_tela_autor(self):
        pass

    def fechar_tela(self):
        self.__manter_tela_aberta = False