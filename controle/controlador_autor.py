from entidade.autor import Autor
from limite.tela_autor import TelaAutor

class ControladorAutor: 

    def __init__(self, controlador_livro):        
        self.__autores = []
        self.__tela_autor = TelaAutor()
        self.__controlador_livro = controlador_livro
        self.__manter_tela_aberta = True

    def abrir_tela_autor(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.incluir_autor, 2: self.listar_autores, 3: self.excluir_autor, 0: self.fechar_tela_autor}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_autor.tela_opcoes()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_autor.aviso_erro()
            else:
                funcao_escolhida()      

        self.__controlador_livro.abrir_tela_livro()

    def incluir_autor(self):
        naoexisteAutor = True
        nome_autor = self.__tela_autor.pega_nome_autor()
        novo_autor = Autor(nome_autor)

        for autor in self.__autores:
            if autor.nome == nome_autor:
                naoexisteAutor = False
        if naoexisteAutor:
            self.__autores.append(novo_autor)
            self.__tela_autor.sucesso_registro()
        else:
            self.__tela_autor.falha_registro()

        return nome_autor

    def listar_autores(self):
        naoexisteAutores = True
        lista_autores = []
        autores = self.__autores
        for autor in autores:
            nome_autor = autor.nome
            lista_autores.append(nome_autor)
            self.__tela_autor.mostra_autor(nome_autor)
            naoexisteAutores = False
        if naoexisteAutores:
            self.__tela_autor.falha_busca()

        return lista_autores

    def excluir_autor(self):
        naoexisteAutor = True
        nome_autor = self.__tela_autor.pega_nome_autor()

        for autor in self.__autores:
            if autor.nome == nome_autor:
                self.__autores.remove(autor)
                naoexisteAutor = False
        if naoexisteAutor:
            self.__tela_autor.falha_exclusao()

    def exclusao_autor(self, autor_excluido):
        for autor in self.__autores:
            if autor.nome == autor_excluido:
                self.__autores.remove(autor)

    def fechar_tela_autor(self):
        self.__manter_tela_aberta = False

