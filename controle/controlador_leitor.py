from limite.tela_leitor import TelaLeitor
from entidade.leitor import Leitor

class ControladorLeitor():
    
    def __init__(self, controlador_principal):
        self.__tela_leitor = TelaLeitor()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True
        self.__leitores = []
        self.notas = {}

    #Espécie de Login
    def selecionar_leitor(self):
        leitores = []
        opcoes = {0: self.abrir_tela_leitor}
        n = 1
        for leitor in self.__leitores:
            opcoes[n] = leitor
            leitores.append(leitor.nome)
            n += 1
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_leitor.selecao_de_leitor(leitores)
            if opcao_escolhida == 0:
                funcao_escolhida = opcoes[opcao_escolhida]  
                funcao_escolhida()
            elif opcao_escolhida != None:   
                try:
                    leitor_escolhido = opcoes[opcao_escolhida]
                except Exception:
                    self.__tela_leitor.aviso_erro(opcao_escolhida)
                else:  
                    self.abrir_menu_leitor(leitor_escolhido)
            else:
                opcoes[0]()


    def cadastrar_leitor(self):
        nome = self.__tela_leitor.cadastro_de_leitor()
        for leitor in self.__leitores:
            if nome == leitor.nome:
                self.__tela_leitor.aviso_erro(nome)
                return
        self.__leitores.append(Leitor(nome))

    #Vê os livros lidos pelo leitor
    def retornar_livros(self, leitor: Leitor):
        livros_lidos = leitor.livros_lidos
        self.__tela_leitor.livros_lidos(livros_lidos)

    #Inclui um novo livro que o leitor leu
    #Não confundir com o cadastro de livros da classe Livro
    def incluir_livro_lido(self, leitor: Leitor):
        livro = self.__controlador_principal.ver_livros()
        livro_nota = self.__tela_leitor.inclusao_de_livro_lido()
        leitor.adicionar_livro(livro, livro_nota)
        if livro in self.notas.keys():
            self.notas[livro].append(livro_nota)
        else:
            self.notas[livro] = [livro_nota]

    def voltar_tela_principal(self):
        self.__manter_tela_aberta = False

    #Menu principal do controlador_leitor
    #Não confundir com o abrir_menu_leitor onde estão as opções do leitor após o 'login'
    def abrir_tela_leitor(self):
        self.__manter_tela_aberta = True
        opcoes = {1: self.selecionar_leitor, 2: self.cadastrar_leitor, 0: self.voltar_tela_principal}   
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_leitor.menu_principal()
            try:
                funcao_escolhida = opcoes[opcao_escolhida]
            except Exception:
                self.__tela_leitor.aviso_erro(opcao_escolhida)
            else:  
                funcao_escolhida()
    
    #Menu específico do leitor
    #Não confundir com o abrir_tela_leitor onde estão as opções de 'login' ou cadastro
    def abrir_menu_leitor(self, leitor: Leitor):
        nome = leitor.nome
        opcoes = {1: self.retornar_livros, 2: self.incluir_livro_lido, 0: self.selecionar_leitor}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_leitor.menu_leitor(nome)
            if opcao_escolhida == 0:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                try:
                    funcao_escolhida = opcoes[opcao_escolhida]
                except Exception:
                    self.__tela_leitor.aviso_erro(opcao_escolhida)
                else:  
                    funcao_escolhida(leitor)