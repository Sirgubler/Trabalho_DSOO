from limite.tela_admin import TelaAdmin

class ControladorAdmin():
    
    def __init__(self, controlador_principal):
        self.__tela_admin = TelaAdmin()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    def abrir_tela_admin(self):
        self.__manter_tela_aberta = True
        senha = self.__tela_admin.login()
        if senha != None and senha == 'Senha123':
            opcoes = {'Cadastrar Crítico': self.cadastrar_critico, 'Voltar': self.voltar_tela_principal}   
            while self.__manter_tela_aberta:
                opcao_escolhida = self.__tela_admin.menu_principal()
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()
        elif senha == None:
            self.__manter_tela_aberta == False
        else:
            self.__tela_admin.aviso(1)

    def cadastrar_critico(self):
        self.__controlador_principal.cadastrar_critico()

    def voltar_tela_principal(self):
        self.__manter_tela_aberta = False
        #teste
