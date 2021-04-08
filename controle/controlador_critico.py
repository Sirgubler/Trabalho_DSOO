from entidade.critico import Critico
from limite.tela_critico import TelaCritico

class ControladorCritico:

    def __init__(self, controlador_principal):
        self.__criticos = []
        self.__tela_critico = TelaCritico()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True
    
    def abrir_tela_critico(self, critico: Critico):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.menu_pesquisar, 2: self.menu_perfil, 3: self.menu_alteracao, 4: self.menu_registrar, 0: self.fechar_tela}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.tela_critico()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_critico.aviso_erro()
            else:
                funcao_escolhida(critico)
        
        self.__controlador_principal.entrar()

    def menu_pesquisar(self, critico: Critico):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.pesquisa_livros, 2: self.pesquisa_autores, 3: self.pesquisa_generos, 4: self.pesquisa_analises, 5: self.pesquisa_usuarios, 0: self.fechar_tela}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_pesquisa()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_critico.aviso_erro()
            else:
                funcao_escolhida(critico)
        
        self.abrir_tela_critico(critico)

    def menu_perfil(self, critico: Critico):
        self__manter_tela_aberta = True
        lista_opcoes = {1: self.perfil_critico, 2: self.perfil_analises, 0: self.fechar_tela}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_perfil()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_critico.aviso_erro
            else:
                funcao_escolhida(critico)
        
        self.abrir_tela_critico(critico)

    def perfil_critico(self, critico: Critico):
        self.__tela_critico.perfil_critico()
        self.menu_perfil(critico)

    def perfil_analises(self, critico: Critico):
        pass

    def menu_alteracao(self, critico: Critico):
        pass

    def menu_registrar(self, critico: Critico):
        pass

    def pesquisa_livros(self, critico: Critico):
        pass

    def pesquisa_autores(self, critico: Critico):
        pass

    def pesquisa_generos(self, critico: Critico):
        pass

    def pesquisa_analises(self, critico: Critico):
        pass

    def pesquisa_usuarios(self, critico: Critico):
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