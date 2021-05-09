from limite.tela_critico import TelaCritico
from entidade.critico import Critico
from persistencia.critico_dao import CriticoDAO
from excecao.usuario_cadastrado import UsuarioCadastrado
from excecao.login_invalido import LoginInvalido

class ControladorCritico():

    def __init__(self, controlador_principal):
        self.__dao = CriticoDAO()
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
                assert LoginInvalido()
            else:
                return

    def cadastrar_critico(self):
        info = self.__tela_critico.cadastro_de_critico()
        if info != None:
            criticos = self.__dao.get_all()
            for critico in criticos:
                if info[0] == critico.nome:
                    assert UsuarioCadastrado(str(type(critico).__name__))
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
        if livro.titulo in critico.livros_analisados.keys():
            alterar = self.__tela_critico.aviso(3)
            if alterar == False:
                return
        if livro == 0:
            return
        else:
            livro_analise = self.__tela_critico.inclusao_de_livro_analisado()
            livro_analise = livro_analise + '\nAnálise por ' + critico.nome + '\n'
            critico.analisar_livro(livro, livro_analise)
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
        opcoes = {'Ver livros analisados': self.retornar_livros, 'Incluir um livro analisado': self.incluir_livro_analisado, 'Alterar Senha': self.alterar_senha, 'Deletar Crítico': self.deletar_critico, 'Voltar': self.abrir_tela_critico}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_critico.menu_critico(nome)
            if opcao_escolhida == 'Voltar':
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida(critico)

    def deletar_critico(self, critico: Critico):
        opcao = self.__tela_critico.deletar_critico(critico.nome)
        if opcao == 'Deletar':
            self.__dao.remove(critico.codigo)
            self.__tela_critico.aviso(4)
            self.abrir_tela_critico()

    def alterar_senha(self, critico: Critico):
        opcao = self.__tela_critico.alterar_senha()
        if opcao[1] == 'Alterar':
            critico.senha = opcao[0][0]
            self.__tela_critico.aviso(5)

    def analises(self):
        criticos = self.__dao.get_all()
        analises = {}
        for critico in criticos:
            for livro in critico.livros_analisados.keys():
                if livro in analises.keys():
                    analises[livro].append(critico.livros_analisados[livro])
                else:
                    analises[livro] = [critico.livros_analisados[livro]]
        return analises
    
    def remover_analise(self, livro):
        criticos = self.__dao.get_all()
        for critico in criticos:
            if livro.titulo in critico.livros_analisados.keys():
                critico.livros_analisados.pop(livro.titulo)
                self.__dao.add(critico)
    
    def alterar_analise(self, livro):
        criticos = self.__dao.get_all()
        for critico in criticos:
            if livro.titulo in critico.livros_analisados.keys():
                for livro_analisado in critico.livros_analisados.keys():
                    if livro_analisado == livro.titulo:
                        livro_analisado = livro.titulo
                        break
                self.__dao.add(critico)
