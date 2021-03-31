from limite.tela_admin import TelaAdmin

class ControladorAdmin():
    
    def __init__(self, controlador_principal):
        self.criticos = []
        self.__tela_admin = TelaAdmin()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    def abrir_tela_admin(self):
        opcoes = {1: self.ver_criticos, 2: self.cadastrar_critico, 0: self.voltar_tela_principal}   
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_admin.menu_principal()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastrar_critico(self):
        pass

    def ver_criticos(self):
        pass

    def voltar_tela_principal(self):
        self.__manter_tela_aberta = False
