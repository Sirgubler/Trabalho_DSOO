from limite.tela_principal import TelaPrincipal
from controle.controlador_leitor import ControladorLeitor
from controle.controlador_livro import ControladorLivro
from controle.controlador_critico import ControladorCritico
from controle.controlador_admin import ControladorAdmin

class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_leitor = ControladorLeitor(self)
        self.__controlador_livro = ControladorLivro(self)
        self.__controlador_critico = ControladorCritico(self)
        self.__controlador_admin = ControladorAdmin(self)

    def iniciar_sistema(self):
        self.abrir_tela()

    def controlador_livro(self):
        print('Menu Livro')
        pass

    def controlador_usuario(self):
        self.abrir_tela_usuario()

    def controlador_leitor(self):
        self.__controlador_leitor.abrir_tela_usuario()

    def controlador_critico(self):
        print('Menu Critico')
        pass

    def controlador_admin(self):
        print('Menu Admin')
        pass

    def encerra_sistema(self):
        exit(0)

    def abrir_tela(self):
    
        opcoes = {1: self.controlador_livro, 2: self.controlador_usuario, 0: self.encerra_sistema}

        while True:

            opcao_escolhida = self.__tela_principal.menu_principal()

            funcao_escolhida = opcoes[opcao_escolhida]

            funcao_escolhida()

    def abrir_tela_usuario(self):

        opcoes = {1: self.controlador_leitor, 2: self.controlador_critico, 3: self.controlador_admin, 0: self.iniciar_sistema}

        while True:

            opcao_escolhida = self.__tela_principal.menu_usuario()

            funcao_escolhida = opcoes[opcao_escolhida]

            funcao_escolhida()