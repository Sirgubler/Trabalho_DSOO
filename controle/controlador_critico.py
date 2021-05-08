from limite.tela_critico import TelaCritico
from entidade.critico import Critico
from persistencia.critico_dao import CriticoDAO

class ControladorCritico():

    def __init__(self, controlador_principal):
        self.__dao = CriticoDAO()
        self.analises = {}
        self.__tela_critico = TelaCritico()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    #Espécie de Login
    def selecionar_critico(self):
        criticos = self.__dao.get_all()
        while self.__manter_tela_aberta:
            critico_escolhido = self.__tela_critico.selecao_de_critico()
            if critico_escolhido != None:
                for critico in criticos:
                    if critico.nome == critico_escolhido[0]:
                        if critico.senha == critico_escolhido[1]:
                            self.abrir_menu_critico(critico)
                            return
                self.__tela_critico.aviso(2)
            else:
                return

    def cadastrar_critico(self):
        info = self.__tela_critico.cadastro_de_critico()
        if info != None:
            criticos = self.__dao.get_all()
            for critico in criticos:
                if info[0] == critico.nome:
                    self.__tela_critico.aviso(3)
                    return
            codigo = (len(self.__dao.get_all()) + 1)
            self.__dao.add(Critico(info[0],info[1],codigo))
            self.__tela_critico.aviso(1)
        else:
            return

    #Vê os livros analisados pelo critico
    def retornar_livros(self, critico: Critico):
        livros = critico.livros_analisados
        self.__tela_critico.livros_analisados(livros)

    #Inclui um novo livro que o critico analisou
    #Não confundir com o cadastro de livros da classe Livro
    def incluir_livro_analisado(self, critico: Critico):
        livro = self.__controlador_principal.ver_livros()
        if livro == 0:
            pass
        else:
            livro_analise = self.__tela_critico.inclusao_de_livro_analisado()
            critico.analisar_livro(livro, livro_analise)
            if livro in self.analises.keys():
                self.analises[livro].append(livro_analise + '\nAnálise por ' + critico.nome + '\n')
            else:
                self.analises[livro] = [livro_analise + '\nAnálise por ' + critico.nome + '\n']
        self.__dao.add(critico)

    def voltar_tela_principal(self):
        self.__manter_tela_aberta = False

    #Menu principal do controlador_critico
    #Não confundir com o abrir_menu_critico onde estão as opções do critico após o 'login'
    def abrir_tela_critico(self):
        self.__manter_tela_aberta = True
        opcoes = {'Login': self.selecionar_critico, 'Voltar': self.voltar_tela_principal}   
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_principal()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()

    #Menu específico do critico
    #Não confundir com o abrir_tela_critico onde estão as opções de 'login' ou cadastro
    def abrir_menu_critico(self, critico: Critico):
        nome = critico.nome
        opcoes = {'Ver livros analisados': self.retornar_livros, 'Incluir um livro analisado': self.incluir_livro_analisado, 'Voltar': self.abrir_tela_critico}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_critico(nome)
            if opcao_escolhida == 'Voltar':
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida(critico)

    def ver_notas(self):
        criticos = self.__dao.get_all()
        for critico in criticos:
            for livro in critico.livros_analisados.keys():
                if livro in self.analises.keys():
                    self.analises[livro].append(critico.livros_analisados[livro])
                else:
                    self.analises[livro] = [critico.livros_analisados[livro]]
