from entidade.critico import Critico
from limite.tela_critico import TelaCritico

class ControladorCritico:

    def __init__(self, controlador_principal):
        self.__criticos = []
        self.__tela_critico = TelaCritico()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True
    
    def abrir_tela_critico(self, critico: Critico):
        pass

    def cadastrar(self):
        naoexisteUsuario = True
        nome = self.__tela_critico.cadastra_nome()
        registro_profissional = self.__tela_critico.cadastra_registro_profissional()
        login = self.__tela_critico.cadastra_login()
        senha = self.__tela_critico.cadastra_senha()
        novo_critico = Critico(nome, registro_profissional)
        usuarios = self.__controlador_principal.logins()
        
        for usuario in usuarios:
            if usuario == login:
                naoexisteUsuario = False
                break
        if naoexisteUsuario:
            novo_critico.login = login
            novo_critico.senha = senha
            self.__criticos.append(novo_critico)
            self.__tela_critico.sucesso_cadastra()
        else:
            self.__tela_critico.erro_cadastra()

    def logins_criticos(self):
        logins_criticos = []
        for critico in self.__criticos:
            logins_criticos.append(critico.login)

        return logins_criticos

    @property
    def criticos(self):
        return self.__criticos

    @criticos.setter
    def criticos(self, criticos: list):
        self.__criticos = criticos

    def fechar_tela(self):
        self.__manter_tela_aberta = False