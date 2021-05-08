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
        self.__manter_tela_aberta = True

    def iniciar_sistema(self):
        self.abrir_tela()

    def controlador_livro(self):
        self.__controlador_livro.abrir_tela_livro()

    def controlador_usuario(self):
        self.abrir_tela_usuario()

    def controlador_leitor(self):
        self.__controlador_leitor.abrir_tela_leitor()

    def controlador_critico(self):
        self.__controlador_critico.abrir_tela_critico()

    def controlador_admin(self):
        self.__controlador_admin.abrir_tela_admin()

    def encerra_sistema(self):
        exit(0)

    #Abre a tela inicial do sistema
    def abrir_tela(self):
        opcoes = {'Menu Livros': self.controlador_livro, 'Menu Usuários': self.controlador_usuario, 'Sair': self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_principal.menu_principal()
            funcao_escolhida = opcoes[opcao_escolhida] 
            funcao_escolhida()

    #Abre a tela de opções de tipo de usuários (leitor, critico e admin)
    def abrir_tela_usuario(self):
        opcoes = {'Menu Leitor': self.controlador_leitor, 'Menu Crítico': self.controlador_critico, 'Menu Admin': self.controlador_admin, 'Voltar': self.iniciar_sistema}
        while True:
            opcao_escolhida = self.__tela_principal.menu_usuario()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastrar_critico(self):
        self.__controlador_critico.cadastrar_critico()
    
    def ver_analises_criticos(self):
        return self.__controlador_critico.analises

    def ver_notas_leitores(self):
        return self.__controlador_leitor.notas

    def ver_livros(self):
        livro = self.__controlador_livro.selecionar_livro()
        return livro
