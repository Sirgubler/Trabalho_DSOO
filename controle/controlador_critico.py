from limite.tela_critico import TelaCritico
from entidade.critico import Critico

class ControladorCritico():

    def __init__(self, controlador_principal):
        self.__criticos = []
        self.analises = {}
        self.__tela_critico = TelaCritico()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    #Espécie de Login
    def selecionar_critico(self):
        criticos = []
        opcoes = {0: self.abrir_tela_critico}
        n = 1
        for critico in self.__criticos:
            opcoes[n] = critico
            criticos.append(critico.nome)
            n += 1
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.selecao_de_critico(criticos)
            if opcao_escolhida == 0:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()
            elif opcao_escolhida != None:
                try:
                    critico_escolhido = opcoes[opcao_escolhida]
                except Exception:
                    self.__tela_critico.aviso_erro(opcao_escolhida)
                else:  
                    self.abrir_menu_critico(critico_escolhido)
            else:
                opcoes[0]()

    def cadastrar_critico(self):
        nome = self.__tela_critico.cadastro_de_critico()
        for critico in self.__criticos:
            if nome == critico.nome:
                self.__tela_critico.aviso_erro(nome)
                return
        self.__criticos.append(Critico(nome))

    #Vê os livros analisados pelo critico
    def retornar_livros(self, critico: Critico):
        livros = critico.livros_analisados
        self.__tela_critico.livros_analisados(livros)

    #Inclui um novo livro que o critico analisou
    #Não confundir com o cadastro de livros da classe Livro
    def incluir_livro_analisado(self, critico: Critico):
        livro_analise = self.__tela_critico.inclusao_de_livro_analisado()
        critico.analisar_livro(livro_analise[0], livro_analise[1])
        if livro_analise[0] in self.analises.keys():
            self.analises[livro_analise[0]].append(livro_analise[1] + '\nAnálise por ' + critico.nome + '\n')
        else:
            self.analises[livro_analise[0]] = [livro_analise[1] + '\nAnálise por ' + critico.nome + '\n']

    def voltar_tela_principal(self):
        self.__manter_tela_aberta = False

    #Menu principal do controlador_critico
    #Não confundir com o abrir_menu_critico onde estão as opções do critico após o 'login'
    def abrir_tela_critico(self):
        self.__manter_tela_aberta = True
        opcoes = {1: self.selecionar_critico, 0: self.voltar_tela_principal}   
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_principal()
            try:
                funcao_escolhida = opcoes[opcao_escolhida]
            except Exception:
                self.__tela_critico.aviso_erro(opcao_escolhida)
            else:  
                funcao_escolhida()

    #Menu específico do critico
    #Não confundir com o abrir_tela_critico onde estão as opções de 'login' ou cadastro
    def abrir_menu_critico(self, critico: Critico):
        nome = critico.nome
        opcoes = {1: self.retornar_livros, 2: self.incluir_livro_analisado, 0: self.selecionar_critico}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_critico(nome)
            if opcao_escolhida == 0:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                try:
                    funcao_escolhida = opcoes[opcao_escolhida]
                except Exception:
                    self.__tela_critico.aviso_erro(opcao_escolhida)
                else:  
                    funcao_escolhida(critico)