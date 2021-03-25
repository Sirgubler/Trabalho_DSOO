from limite.tela_leitor import TelaLeitor

class ControladorLeitor():
    
    def __init__(self, controlador_principal):
        self.livros = []
        self.__tela_leitor = TelaLeitor()
        self.__manter_tela_aberta = True

    def selecionar_leitor(self):
        self.__tela_leitor.selecao_de_leitor(self.livros)

    def cadastrar_leitor(self):
        pass

    def voltar_tela_principal(self):
        self.__manter_tela_aberta = False

    def abrir_tela_usuario(self):
        opcoes = {1: self.selecionar_leitor, 2: self.cadastrar_leitor, 0: self.voltar_tela_principal}

        while self.__manter_tela_aberta:

            opcao_escolhida = self.__tela_leitor.menu_principal()

            funcao_escolhida = opcoes[opcao_escolhida]

            funcao_escolhida()