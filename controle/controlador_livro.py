from entidade.livro import Livro
from limite.tela_livro import TelaLivro
from controle.controlador_autor import ControladorAutor
from controle.controlador_genero import ControladorGenero
from controle.controlador_principal import ControladorPrincipal

class ControladorLivro():
    def __init__(self, controlador_principal: ControladorPrincipal):
        self.__livros = []
        self.__tela_livro = TelaLivro()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = None

    def abrir_tela_livro(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_livro, 2: self.remover_livro, 3: self.listar_livros, 4: self.pesquisar_livro_por_titulo, 5: self.ver_analises, 6: self.verificar_notas, 0: self.fechar_tela_livro}

        while self.__manter_tela_aberta:
            lista_opcoes[self.__tela_livro.tela_opcoes()]()

        if self.__manter_tela_aberta == False:
            self.__controlador_principal.abrir_tela()
                        
    def cadastrar_livro(self):
        naoexisteLivro = True
        dados_livro = self.__tela_livro.pega_dados_livro()
        novo_livro = Livro(dados_livro["nome"], dados_livro["autor"], dados_livro["genero"])
        for livro in self.__livros:
            if livro.nome == novo_livro.nome and livro.autor == novo_livro.autor and livro.genero == novo_livro.genero:
                naoexisteLivro = False
        if naoexisteLivro:
            self.__livros.append(novo_livro)


    def remover_livro(self):
        dados_livros = self.__tela_livro.pega_dados_livro()
        for livro in self.__livros:
            if livro.nome == dados_livros["nome"] and livro.autor == dados_livros["autor"] and livro.genero == dados_livros["genero"]:
                del(self.__livros[livro])
                            

    def listar_livros(self):
        pass

    def pesquisar_livro_por_titulo(self):
        pass

    def ver_analises(self):
        pass

    def verificar_notas(self):
        pass

    def fechar_tela_livro(self):
        pass