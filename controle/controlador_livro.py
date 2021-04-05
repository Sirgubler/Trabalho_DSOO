from entidade.livro import Livro
from limite.tela_livro import TelaLivro
from controle.controlador_autor import ControladorAutor
from controle.controlador_genero import ControladorGenero

class ControladorLivro():

    def __init__(self, controlador_principal):
        self.__livros = []
        self.__tela_livro = TelaLivro()
        self.__controlador_autor = ControladorAutor(self)
        self.__controlador_genero = ControladorGenero(self)
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    def abrir_tela_livro(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_livro, 2: self.listar_livros, 3: self.remover_livro, 4: self.pesquisar_livro_por_titulo, 5: self.pesquisar_livro_por_autor, 6: self.pesquisar_livro_por_genero, 7: self.ver_analises, 8: self.verificar_notas, 9: self.menu_autor, 10: self.menu_genero, 0: self.fechar_tela_livro}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_livro.tela_opcoes()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_livro.aviso_erro()
            else:
                funcao_escolhida()      

        self.__controlador_principal.abrir_tela()

    def cadastrar_livro(self):
        naoexisteLivro = True
        titulo_do_livro = self.__tela_livro.cadastro_livro()
        autor_do_livro = self.__controlador_autor.incluir_autor()
        genero_do_livro = self.__controlador_genero.incluir_genero()
        novo_livro = Livro(titulo_do_livro, autor_do_livro, genero_do_livro)

        for livro in self.__livros:
            if livro.titulo == titulo_do_livro:
                naoexisteLivro = False
        if naoexisteLivro:
            self.__livros.append(novo_livro)
            self.__tela_livro.sucesso_registro()
        else:
            self.__tela_livro.falha_registro()

        return titulo_do_livro

    def listar_livros(self):
        naoexisteLivro = True
        lista_livros = []   
        for livro in self.__livros:
            titulo_do_livro = livro.titulo
            autor_do_livro = livro.autor
            genero_do_livro = livro.genero
            lista_livros.append(livro.titulo)
            dados_livro = {'titulo': titulo_do_livro, 'autor': autor_do_livro, 'genero': genero_do_livro}
            self.__tela_livro.mostra_livro(dados_livro)
            naoexisteLivro = False
        if naoexisteLivro:
            self.__tela_livro.falha_busca()
        
        return lista_livros

    def remover_livro(self):
        naoexisteLivro = True
        titulo_do_livro = self.__tela_livro.exclusao_livro()
        for livro in self.__livros:
            if livro.titulo == titulo_do_livro:
                autor_do_livro = livro.autor
                genero_do_livro = livro.genero
                self.__controlador_autor.exclusao_autor(autor_do_livro)
                self.__controlador_genero.exclusao_genero(genero_do_livro)
                self.__livros.remove(livro)
                naoexisteLivro = False
        if naoexisteLivro:
            self.__tela_livro.falha_exclusao()

    def pesquisar_livro_por_titulo(self):
        naoexisteLivro = True
        busca = self.__tela_livro.pesquisa_titulo()
        resultado = None
        for livro in self.__livros:
            if livro.titulo == busca:
                naoexisteLivro = False
                titulo_do_livro = livro.titulo
                autor_do_livro = livro.autor
                genero_do_livro = livro.genero
                resultado = {'titulo': titulo_do_livro, 'autor': autor_do_livro, 'genero': genero_do_livro}
                self.__tela_livro.mostra_livro({'titulo': titulo_do_livro, 'autor': autor_do_livro, 'genero': genero_do_livro})
        if naoexisteLivro:
            self.__tela_livro.falha_busca()

        return resultado

    def pesquisar_livro_por_autor(self):
        naoexisteLivro = True
        busca = self.__tela_livro.pesquisa_autor()
        resultados = []
        for livro in self.__livros:
            if livro.autor == busca:
                naoexisteLivro = False
                titulo_do_livro = livro.titulo
                autor_do_livro = livro.autor
                genero_do_livro = livro.genero
                resultado = {'titulo': titulo_do_livro, 'autor': autor_do_livro, 'genero': genero_do_livro}
                resultados.append(resultado)
                self.__tela_livro.mostra_livro({'titulo': titulo_do_livro, 'autor': autor_do_livro, 'genero': genero_do_livro})
        if naoexisteLivro:
            self.__tela_livro.falha_busca()
        
        return resultados

    def pesquisar_livro_por_genero(self):
        naoexisteLivro = True
        busca = self.__tela_livro.pesquisa_genero()
        resultados = []
        for livro in self.__livros:
            if livro.genero == busca:
                naoexisteLivro = False
                titulo_do_livro = livro.titulo
                autor_do_livro = livro.autor
                genero_do_livro = livro.genero
                resultado = {'titulo': titulo_do_livro, 'autor': autor_do_livro, 'genero': genero_do_livro}
                resultados.append(resultado)
                self.__tela_livro.mostra_livro({'titulo': titulo_do_livro, 'autor': autor_do_livro, 'genero': genero_do_livro})
        if naoexisteLivro:
            self.__tela_livro.falha_busca()

        return resultados

    def ver_analises(self):
        analises = self.__controlador_principal.ver_analises_criticos()
        self.__tela_livro.mostra_analises(analises)

    def verificar_notas(self):
        notas_livros = self.__controlador_principal.ver_notas_leitores()
        media_livros = {}
        for livro in notas_livros.keys():
            media_livros[livro] = sum(notas_livros[livro])/len(notas_livros[livro])
        self.__tela_livro.mostra_media(media_livros)


    def menu_autor(self):
        self.__controlador_autor.abrir_tela_autor()

    def menu_genero(self):
        self.__controlador_genero.abrir_tela_genero()

    def fechar_tela_livro(self):
        self.__manter_tela_aberta = False