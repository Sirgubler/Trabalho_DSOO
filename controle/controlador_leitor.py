from limite.tela_leitor import TelaLeitor
from entidade.leitor import Leitor
from persistencia.leitor_dao import LeitorDAO
from excecao.usuario_cadastrado import UsuarioCadastrado
from excecao.login_invalido import LoginInvalido

class ControladorLeitor():
    
    def __init__(self, controlador_principal):
        self.__tela_leitor = TelaLeitor()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True
        self.__dao = LeitorDAO()

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
                assert LoginInvalido()
            else:
                return

    def cadastrar_leitor(self):
        info = self.__tela_leitor.cadastro_de_leitor()
        if info != None:
            leitores = self.__dao.get_all()
            for leitor in leitores:
                if info[0] == leitor.nome:
                    assert UsuarioCadastrado(str(type(leitor).__name__))
                    return
            leitores = list(self.__dao.get_all())
            if leitores == []:
                codigo = 1
            else:
                codigo = leitores[-1].codigo + 1
            self.__dao.add(Leitor(info[0],info[1],codigo))
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
        if livro.titulo in leitor.livros_lidos.keys():
            alterar = self.__tela_leitor.aviso(3)
            if alterar == False:
                return
        if livro == 0:
            return
        else:
            livro_nota = self.__tela_leitor.inclusao_de_livro_lido()
            leitor.adicionar_livro(livro.titulo, livro_nota)
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
        opcoes = {'Ver livros lidos': self.retornar_livros, 'Incluir um livro lido': self.incluir_livro_lido, 'Alterar Senha': self.alterar_senha, 'Deletar Leitor': self.deletar_leitor, 'Voltar': self.abrir_tela_leitor}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_leitor.menu_leitor(nome)
            if opcao_escolhida == 'Voltar':
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida(leitor)

    def deletar_leitor(self, leitor: Leitor):
        opcao = self.__tela_leitor.deletar_leitor(leitor.nome)
        if opcao == 'Deletar':
            self.__dao.remove(leitor.codigo)
            self.__tela_leitor.aviso(4)
            self.abrir_tela_leitor()

    def alterar_senha(self, leitor: Leitor):
        opcao = self.__tela_leitor.alterar_senha()
        if opcao[1] == 'Alterar':
            leitor.senha = opcao[0][0]
            self.__tela_leitor.aviso(5)
            self.__dao.add(leitor)

    def notas(self):
        leitores = self.__dao.get_all()
        notas = {}
        for leitor in leitores:
            for livro in leitor.livros_lidos.keys():
                if livro in notas.keys():
                    notas[livro].append(leitor.livros_lidos[livro])
                else:
                    notas[livro] = [leitor.livros_lidos[livro]]
        return notas

    def remover_nota(self, livro):
        leitores = self.__dao.get_all()
        for leitor in leitores:
            if livro.titulo in leitor.livros_lidos.keys():
                leitor.livros_lidos.pop(livro.titulo)
                self.__dao.add(leitor)