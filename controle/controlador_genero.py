from entidade.genero import Genero
from limite.tela_genero import TelaGenero

class ControladorGenero: 

    def __init__(self, controlador_livro):        
        self.__generos = []
        self.__tela_genero = TelaGenero()
        self.__controlador_livro = controlador_livro
        self.__manter_tela_aberta = True

    def abrir_tela_genero(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.incluir_genero, 2: self.listar_generos, 3: self.excluir_genero, 0: self.fechar_tela_genero}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_genero.tela_opcoes()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_genero.aviso_erro()
            else:
                funcao_escolhida()      

        self.__controlador_livro.abrir_tela_livro()

    def incluir_genero(self):
        naoexisteGenero = True
        nome_genero = self.__tela_genero.pega_nome_genero()
        novo_genero = Genero(nome_genero)

        for genero in self.__generos:
            if genero.nome == nome_genero:
                naoexisteGenero = False
        if naoexisteGenero:
            self.__generos.append(novo_genero)
            self.__tela_genero.sucesso_registro()
        else:
            self.__tela_genero.falha_registro()

        return nome_genero

    def listar_generos(self):
        naoexisteGenero = True
        lista_generos = []
        generos = self.__generos
        for genero in generos:
            nome_genero = genero.nome
            lista_generos.append(nome_genero)
            self.__tela_genero.mostra_genero(nome_genero)
            naoexisteGenero = False
        if naoexisteGenero:
            self.__tela_genero.falha_busca()
        
        return lista_generos

    def excluir_genero(self):
        naoexisteGenero = True
        nome_genero = self.__tela_genero.pega_nome_genero()

        for genero in self.__generos:
            if genero.nome == nome_genero:
                self.__generos.remove(genero)
                naoexisteGenero = False
        if naoexisteGenero:
            self.__tela_genero.falha_exclusao()

    def exclusao_genero(self, genero_excluido):
        for genero in self.__generos:
            if genero.nome == genero_excluido:
                self.__generos.remove(genero)

    def fechar_tela_genero(self):
        self.__manter_tela_aberta = False