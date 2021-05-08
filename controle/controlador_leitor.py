from limite.tela_leitor import TelaLeitor
from entidade.leitor import Leitor
from persistencia.leitor_dao import LeitorDAO

class ControladorLeitor():
    
    def __init__(self, controlador_principal):
        self.__tela_leitor = TelaLeitor()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True
        self.__dao = LeitorDAO()
        self.notas = {}

    #Espécie de Login
    def selecionar_leitor(self):
        leitores = self.__dao.get_all()
        while self.__manter_tela_aberta:
            leitor_escolhido = self.__tela_leitor.selecao_de_leitor()
            if leitor_escolhido != None:
                for leitor in leitores:
                    if leitor.nome == leitor_escolhido[0]:
                        if leitor.senha == leitor_escolhido[1]:
                            self.abrir_menu_leitor(leitor)
                            return
                self.__tela_leitor.aviso(2)
            else:
                return

    def cadastrar_leitor(self):
        info = self.__tela_leitor.cadastro_de_leitor()
        if info != None:
            leitores = self.__dao.get_all()
            for leitor in leitores:
                if info[0] == leitor.nome:
                    self.__tela_leitor.aviso(3)
                    return
            codigo = (len(self.__dao.get_all()) + 1)
            self.__dao.add(Leitor(info[0],info[1],codigo))
            self.__tela_leitor.aviso(1)
        else:
            return

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
        self.__dao.add(leitor)

    def voltar_tela_principal(self):
        self.__manter_tela_aberta = False

    #Menu principal do controlador_leitor
    #Não confundir com o abrir_menu_leitor onde estão as opções do leitor após o 'login'
    def abrir_tela_leitor(self):
        self.__manter_tela_aberta = True
        opcoes = {'Login': self.selecionar_leitor,'Cadastro': self.cadastrar_leitor, 'Voltar': self.voltar_tela_principal}   
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_leitor.menu_principal()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()
    
    #Menu específico do leitor
    #Não confundir com o abrir_tela_leitor onde estão as opções de 'login' ou cadastro
    def abrir_menu_leitor(self, leitor: Leitor):
        nome = leitor.nome
        opcoes = {'Ver livros lidos': self.retornar_livros, 'Incluir um livro lido': self.incluir_livro_lido, 'Voltar': self.abrir_tela_leitor}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_leitor.menu_leitor(nome)
            if opcao_escolhida == 'Voltar':
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida(leitor)

    def ver_notas(self):
        leitores = self.__dao.get_all()
        for leitor in leitores:
            for livro in leitor.livros_lidos.keys():
                if livro in self.notas.keys():
                    self.notas[livro].append(leitor.livros_lidos[livro])
                else:
                    self.notas[livro] = [leitor.livros_lidos[livro]]