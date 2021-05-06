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

    def controlador_autor(self):
        self.__controlador_autor.abrir_tela_autor()

    def controlador_genero(self):
        self.__controlador_genero.abrir_tela_genero()

    def abrir_tela_livro(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {'Cadastrar Livro': self.cadastrar_livro, 'Alterar Livro': self.alterar_livro, 'Listar Livros': self.listar_livros, 'Remover Livro': self.remover_livro, 'Pesquisar Livros': self.pesquisar_livros, 'Verificar Analises': self.verificar_analises, 'Verificar Notas': self.verificar_notas, 'Menu Autor': self.controlador_autor, 'Menu Genero': self.controlador_genero, 'Voltar': self.fechar_tela_livro}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_livro.menu_livro()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_livro.aviso_erro()
            else:
                funcao_escolhida()      

        self.__controlador_principal.abrir_tela()

    def cadastrar_livro(self):
        naoexisteLivro = True
        dados_livro = self.__tela_livro.cadastro_livro()
        
        if dados_livro != None:
            titulo = dados_livro['titulo']
            autor = dados_livro['autor']
            genero = dados_livro['genero']
            self.__controlador_autor.naoexisteAutor(autor)
            self.__controlador_genero.naoexisteGenero(genero)
            
            for livro in self.__livros:
                if livro.titulo == titulo:
                    naoexisteLivro = False
                    break
            if naoexisteLivro:
                novo_livro = Livro(titulo, autor, genero)
                self.__livros.append(novo_livro)
        
        self.abrir_tela_livro()

    def alterar_livro(self):
        existeLivro = False
        titulo = self.__tela_livro.busca_titulo()
        livro_encontrado = None

        for livro in self.__livros:
            if livro.titulo == titulo:
                existeLivro = True
                livro_encontrado = livro
                break
        if existeLivro:
            alteracao_escolhida = self.__tela_livro.altera_livro()
            if alteracao_escolhida == 'Alterar Titulo':
                novo_titulo = self.__tela_livro.altera_titulo()
                livro_encontrado.titulo = novo_titulo
            if alteracao_escolhida == 'Alterar Autor':
                autor = self.__controlador_autor.alterar_autor_livro()
                livro_encontrado.autor = autor
            if alteracao_escolhida == 'Alterar Genero':
                genero = self.__controlador_genero.alterar_genero_livro()
                livro_encontrado.genero = genero
            if alteracao_escolhida == 'Voltar':
                self.alterar_livro()
        else:
            self.__tela_livro.aviso_erro()
        
        self.abrir_tela_livro()

    def listar_livros(self):
        livros = []
        for livro in self.__livros:
            livros.append(livro.titulo)

        livro_escolhido = self.__tela_livro.lista_livros(livros)
        if livro_escolhido != None:
            titulo = livro.titulo
            autor = livro.autor.nome
            genero = livro.genero.nome
            dados_livro = [titulo, autor, genero]
            mostrar_livro = self.__tela_livro.mostra_livro(dados_livro)
            if mostrar_livro == None:
                self.listar_livros
        
        self.abrir_tela_livro()

    def remover_livro(self):
        naoexisteLivro = True
        titulo = self.__tela_livro.remove_livro()

        for livro in self.__livros:
            if livro.titulo == titulo:
                naoexisteLivro = False
                self.__livros.remove(livro)
                break
        if naoexisteLivro:
            self.__tela_livro.aviso_erro()
        
        self.abrir_tela_livro()
        
    def pesquisar_livros(self):
        pass

    def verificar_analises(self):
        pass

    def verificar_notas(self):
        pass

    def fechar_tela_livro(self):
        self.__manter_tela_aberta = False