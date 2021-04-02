from limite.tela_critico import TelaCritico
from entidade.critico import Critico

class ControladorCritico():
    
    def __init__(self, controlador_principal):
        self.criticos = []
        self.__tela_critico = TelaCritico()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    #Espécie de Login
    def selecionar_critico(self):
        criticos = []
        opcoes = {0: self.abrir_tela_critico}
        for critico in self.criticos:
            n = 1
            opcoes[n] = critico
            criticos.append(critico.nome)
            n += 1
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.selecao_de_critico(criticos)
            if opcao_escolhida != 0:
                critico_escolhido = opcoes[opcao_escolhida]
                self.abrir_menu_critico(critico_escolhido)
            else:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()

    def cadastrar_critico(self):
        nome = self.__tela_critico.cadastro_de_critico()
        critico = Critico(nome)
        self.criticos.append(critico)

    #Vê os livros analisados pelo critico
    def retornar_livros(self, critico: Critico):
        livros_analisados = {}
        for livro in critico.livros_analisados:
            livros_analisados[livro.livro] = livro.texto
        self.__tela_critico.livros_analisados(livros_analisados)

    #Inclui um novo livro que o critico analisou
    #Não confundir com o cadastro de livros da classe Livro
    def incluir_livro_analisado(self, critico: Critico):
        livro_analise = self.__tela_critico.inclusao_de_livro_analisado()
        critico.analisar_livro(livro_analise[0], livro_analise[1])

    def voltar_tela_principal(self):
        self.__manter_tela_aberta = False

    #Menu principal do controlador_critico
    #Não confundir com o abrir_menu_critico onde estão as opções do critico após o 'login'
    def abrir_tela_critico(self):
        self.__manter_tela_aberta = True
        opcoes = {1: self.selecionar_critico, 0: self.voltar_tela_principal}   
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_principal()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()

    #Menu específico do critico
    #Não confundir com o abrir_tela_critico onde estão as opções de 'login' ou cadastro
    def abrir_menu_critico(self, critico: Critico):
        nome = critico.nome
        opcoes = {1: self.retornar_livros, 2: self.incluir_livro_analisado, 0: self.selecionar_critico}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_critico(nome)
            if opcao_escolhida != 0:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida(critico)
            else:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()