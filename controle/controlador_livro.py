from entidade.livro import Livro
from limite.tela_livro import TelaLivro
from controle.controlador_autor import ControladorAutor
from controle.controlador_genero import ControladorGenero
from controle.controlador_principal import ControladorPrincipal
from entidade.critico import Critico
from controle.controlador_critico import ControladorCritico
from controle.controlador_leitor import ControladorLeitor
class ControladorLivro():
    def __init__(self, controlador_principal: ControladorPrincipal):
        self.__livros = []
        self.__tela_livro = TelaLivro()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True
        self.__controlador_critico = ControladorCritico
        self.__controlador_leitor = ControladorLeitor

    def abrir_tela_livro(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_livro, 2: self.remover_livro, 3: self.listar_livros, 4: self.pesquisar_livro_por_titulo, 5: self.ver_analises, 6: self.verificar_notas, 0: self.fechar_tela_livro}

        while self.__manter_tela_aberta:
            lista_opcoes[self.__tela_livro.tela_opcoes()]()

        self.__controlador_principal.abrir_tela()

    def cadastrar_livro(self):
        naoexisteLivro = True
        dados_livro = self.__tela_livro.cadastro_livro()
        novo_livro = Livro(dados_livro["nome"], dados_livro["autor"], dados_livro["genero"])
        for livro in self.__livros:
            if livro.nome == novo_livro.nome and livro.autor == novo_livro.autor and livro.genero == novo_livro.genero:
                naoexisteLivro = False
        if naoexisteLivro:
            self.__livros.append(novo_livro)


    def remover_livro(self):
        dados_livros = self.__tela_livro.exclusao_livro()
        for livro in self.__livros:
            if livro.nome == dados_livros["nome"] and livro.autor == dados_livros["autor"] and livro.genero == dados_livros["genero"]:
                self.__livros.remove(livro)

    def listar_livros(self):
        for livro in self.__livros:
            self.__tela_livro.mostra_livro({"nome": livro.nome, "autor": livro.autor, "genero": livro.genero})

    def pesquisar_livro_por_titulo(self):
        busca = self.__tela_livro.pesquisar_livro()
        for livro in self.__livros:
            if livro.nome == busca["nome"]:
                self.__tela_livro.mostra_livro({"nome": livro.nome, "autor": livro.autor, "genero": livro.genero})

    
    def ver_analises(self):
        criticos_existentes = self.__controlador_critico.criticos
        for critico in criticos_existentes:
            for analise in critico.livros_analisados:
                dados_da_analise = {"analise": analise.texto, "livro": analise.livro}
                self.__tela_livro.mostra_analise(dados_da_analise)
                for livro in self.__livros:
                    if livro.nome == analise.livro:
                        pessoa = critico.nome
                        comentario = analise.livro
                        livro.adicionar_analise(pessoa,comentario)

    def verificar_notas(self):
        leitores_existentes = self.__controlador_leitor.leitores
        for leitor in leitores_existentes:
            for leitura in leitor.livros_lidos():
                dados_da_nota = {"livro": leitura.texto, "nota": leitura.livro}
                self.__tela_livro.mostra_nota(dados_da_nota)
                for livro in self.__livros:
                    if livro.nome == leitura.livro:
                        pessoa = leitor.nome
                        avaliacao = leitura.nota
                        livro.adicionar_avaliacao(pessoa,avaliacao)


    def fechar_tela_livro(self):
        self.__manter_tela_aberta = False