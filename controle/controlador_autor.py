from entidade.autor import Autor
from limite.tela_autor import TelaAutor
from controle.controlador_livro import ControladorLivro

class ControladorAutor:   
    def __init__(self, controlador_livro: ControladorLivro):        
        self.__autores = []
        self.__tela_autor = TelaAutor()
        self.__controlador_livro = controlador_livro

    def abrir_tela_autor(self):
        lista_opcoes = {1: self.incluir_autor, 2: self.listar_autores}
        continua = True

        while continua:
            lista_opcoes[self.__tela_autor.tela_opcoes()]()

    def incluir_autor(self):
        naoexisteAutor = True
        dados_autor = self.__tela_autor.pega_dados_autor()
        novo_autor = Autor(dados_autor["nome"])
        for autor in self.__autores:
            if autor.nome == novo_autor.nome:
                naoexisteAutor = False
        if naoexisteAutor:
            self.__autores.append(novo_autor)

    def listar_autores(self):
        for autor in self.__autores:
            self.__tela_autor.mostra_autor({"nome": autor.nome})