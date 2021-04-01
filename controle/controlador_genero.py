from entidade.genero import Genero
from limite.tela_genero import TelaGenero
from controle.controlador_livro import ControladorLivro

class ControladorGenero:    
    def __init__(self, controlador_livro: ControladorLivro):        
        self.__generos = []
        self.__tela_genero = TelaGenero()
        self.__controlador_livro = controlador_livro


    def abrir_tela_genero(self):
        lista_opcoes = {1: self.incluir_genero, 2: self.listar_generos, 0: self.fechar_tela_genero}
        continua = True

        while continua:
            lista_opcoes[self.__tela_genero.tela_opcoes()]()

    def incluir_genero(self):
        naoexisteGenero = True
        dados_genero = self.__tela_genero.pega_dados_genero()
        novo_genero = Genero(dados_genero["nome"])
        for genero in self.__generos:
            if genero.nome == novo_genero.nome:
                naoexisteGenero = False
        if naoexisteGenero:
            self.__generos.append(novo_genero)

    def listar_generos(self):
        for genero in self.__generos:
            self.__tela_genero.mostra_genero({"nome": genero.nome})

    def fechar_tela_genero(self):
        self.abrir_tela_genero().continua = False
        self.__controlador_livro.abrir_tela_livro