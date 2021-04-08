from entidade.leitor import Leitor
from limite.tela_leitor import TelaLeitor

class ControladorLeitor:

    def __init__(self, controlador_principal):
        self.__leitores = []
        self.__tela_leitor = TelaLeitor()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True
    
    def abrir_tela_leitor(self, leitor: Leitor):
        pass
    
    def cadastrar(self):
        naoexisteUsuario = True
        nome = self.__tela_leitor.cadastra_nome()
        login = self.__tela_leitor.cadastra_login()
        senha = self.__tela_leitor.cadastra_senha()
        novo_leitor = Leitor(nome)
        usuarios = self.__controlador_principal.logins()
        
        for usuario in usuarios:
            if usuario == login:
                naoexisteUsuario = False
                break
        if naoexisteUsuario:
            novo_leitor.login = login
            novo_leitor.senha = senha
            self.__leitores.append(novo_leitor)
            self.__tela_leitor.sucesso_cadastra()
        else:
            self.__tela_leitor.erro_cadastra()

    def logins_leitores(self):
        logins_leitores = []
        for leitor in self.__leitores:
            logins_leitores.append(leitor.login)

        return logins_leitores

    @property
    def leitores(self):
        return self.__leitores

    @leitores.setter
    def leitores(self, leitores: list):
        self.__leitores = leitores

    def fechar_tela(self):
        self.__manter_tela_aberta = False