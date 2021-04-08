from controle.controlador_livro import ControladorLivro
from controle.controlador_leitor import ControladorLeitor
from controle.controlador_critico import ControladorCritico
from controle.controlador_sistema import ControladorSistema
from limite.tela_principal import TelaPrincipal

class ControladorPrincipal:

    def __init__(self):
        self.__analises = []
        self.__tela_principal = TelaPrincipal()
        self.__controlador_livro = ControladorLivro(self)
        self.__controlador_leitor = ControladorLeitor(self)
        self.__controlador_critico = ControladorCritico(self)
        self.__controlador_sistema = ControladorSistema(self)
        self.__manter_tela_aberta = True

    def iniciar_sistema(self):
        self.abrir_tela_principal()

    def abrir_tela_principal(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.cadastrar, 2:self.entrar, 3: self.visitar, 0: self.encerrar_sistema}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_principal.tela_principal()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_principal.aviso_erro()
            else:
                funcao_escolhida()

    def cadastrar(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.signupar, 0: self.fechar_tela}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_principal.cadastra()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_principal.aviso_erro()
            else:
                funcao_escolhida()

        self.abrir_tela_principal()

    def signupar(self):
        self.__manter_tela_aberta
        lista_opcoes = {1: self.__controlador_critico.cadastrar, 2: self.__controlador_leitor.cadastrar, 0: self.fechar_tela}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_principal.signupa()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_principal.aviso_erro()
            else:
                funcao_escolhida()

        self.abrir_tela_principal()
    
    def entrar(self):
        self.__manter_tela_aberta = True
        lista_opcoes =  {1: self.logar, 0: self.fechar_tela}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_principal.entra()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_principal.aviso_erro()
            else:
                funcao_escolhida()

        self.abrir_tela_principal()

    def logar(self):
        existeLeitor = False
        existeCritico = False
        login = self.__tela_principal.loga_nome()
        senha = self.__tela_principal.loga_senha()
        leitor_encontrado = None
        critico_encontrado = None
        for leitor in self.__controlador_leitor.leitores:
            if leitor.login == login and leitor.senha == senha:
                leitor_encontrado = leitor
                existeLeitor = True
                break
        for critico in self.__controlador_critico.criticos:
            if critico.login == login and critico.senha == senha:
                critico_encontrado = critico
                existeCritico = True
                break
        if existeLeitor:
            self.__controlador_leitor.abrir_tela_leitor(leitor_encontrado)
        if existeCritico:
            self.__controlador_critico.abrir_tela_critico(critico_encontrado)
        else:
            self.__tela_principal.erro_logar()
    
    def visitar(self):
        pass

    def logins(self):
        usuarios = []
        logins_criticos = self.__controlador_critico.logins_criticos()
        logins_leitores = self.__controlador_leitor.logins_leitores()
        for login_critico in logins_criticos:
            usuarios.append(login_critico)
        for login_leitor in logins_leitores:
            usuarios.append(login_leitor)

        return usuarios

    def fechar_tela(self):
        self.__manter_tela_aberta = False

    def encerrar_sistema(self):
        exit(0)