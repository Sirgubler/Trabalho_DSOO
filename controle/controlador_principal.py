from limite.tela_principal import TelaPrincipal
from controle.controlador_leitor import ControladorLeitor

class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_leitor = ControladorLeitor(self)

    def inicializa_sistema(self):
        self.abre_tela_principal()

    def livro(self):
        print('Menu Livro')
        pass

    def usuario(self):
        self.abre_tela_usuario()

    def leitor(self):
        print('Menu Leitor')
        pass

    def critico(self):
        print('Menu Critico')
        pass

    def admin(self):
        print('Menu Admin')
        pass

    def encerra_sistema(self):
        exit(0)

    def abre_tela_principal(self):
    
        opcoes = {1: self.livro, 2: self.usuario, 0: self.encerra_sistema}

        while True:

            opcao_escolhida = self.__tela_principal.menu_principal()

            funcao_escolhida = opcoes[opcao_escolhida]

            funcao_escolhida()

    def abre_tela_usuario(self):

        opcoes = {1: self.leitor, 2: self.critico, 3: self.admin, 0: self.inicializa_sistema}

        while True:

            opcao_escolhida = self.__tela_principal.menu_usuario()

            funcao_escolhida = opcoes[opcao_escolhida]

            funcao_escolhida()