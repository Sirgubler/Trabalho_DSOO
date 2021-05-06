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
            autor_escolhido = self.__controlador_autor.naoexisteAutor(autor)
            genero_escolhido = self.__controlador_genero.naoexisteGenero(genero)
            
            for livro in self.__livros:
                if livro.titulo == titulo:
                    naoexisteLivro = False
                    break
            if naoexisteLivro:
                novo_livro = Livro(titulo, autor_escolhido, genero_escolhido)
                self.__livros.append(novo_livro)
        
        self.abrir_tela_livro()

    def alterar_livro(self):
        self.__manter_tela_aberta = True
        existeLivro = False
        titulo = self.__tela_livro.busca_titulo()
        livro_encontrado = None

        for livro in self.__livros:
            if livro.titulo == titulo:
                existeLivro = True
                livro_encontrado = livro
                break
        if existeLivro:
            self.__manter_tela_aberta = True
            lista_opcoes = {'Alterar Titulo': self.altera_titulo, 'Alterar Autor': self.altera_autor, 'Alterar Genero': self.altera_genero, 'Cancelar': self.fechar_tela_livro}
            while self.__manter_tela_aberta:
                opcao_escolhida = self.__tela_livro.altera_livro()
                if opcao_escolhida == 'Cancelar':
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                elif opcao_escolhida != 'Cancelar':
                    try:
                        funcao_escolhida = lista_opcoes[opcao_escolhida]
                    except Exception:
                        self.__tela_livro.aviso_erro()
                    else:
                        funcao_escolhida(livro_encontrado)
                else:
                    self.alterar_livro()      

        self.abrir_tela_livro()
    
    def altera_titulo(self, livro_encontrado: Livro):
        naoexisteTitulo = True
        titulo_alterado = self.__tela_livro.altera_titulo()

        for livro in self.__livros:
            if livro.titulo == titulo_alterado:
                naoexisteTitulo = False
                self.__tela_livro.aviso_erro()
                break
        if naoexisteTitulo:
            livro_encontrado.titulo = titulo_alterado
            self.__tela_livro.aviso_sucesso()
    
    def altera_autor(self, livro_encontrado: Livro):
        novo_autor = self.__controlador_autor.alterar_autor_livro()
        for livro in self.__livros:
            if livro.titulo == livro_encontrado.titulo:
                livro.autor = novo_autor

    def altera_genero(self, livro_encontrado):
        novo_genero = self.__controlador_genero.alterar_genero_livro()
        livro_encontrado.genero = novo_genero

    def listar_livros(self):
        livros = []

        for livro in self.__livros:
            livros.append(livro.titulo)

        livro_escolhido = self.__tela_livro.lista_livros(livros)
        if livro_escolhido != 'Voltar':
            self.mostrar_livro(livro_escolhido)
        else:
            self.abrir_tela_livro()

    def mostrar_livro(self, livro_escolhido):
        existeLivro = False        
        dados_livro = {}
        livro_encontrado = None

        for livro in self.__livros:
            if livro.titulo == livro_escolhido:
                existeLivro = True
                livro_encontrado = livro
                break
        if existeLivro:
            titulo = livro_encontrado.titulo
            autor_objeto = livro_encontrado.autor
            genero_objeto = livro_encontrado.genero
            autor = self.__controlador_autor.pega_nome(autor_objeto)
            genero = self.__controlador_genero.pega_nome(genero_objeto)
            dados_livro = {'titulo': titulo, 'autor': autor, 'genero': genero}
            self.__tela_livro.mostra_livro(dados_livro)
           
        self.listar_livros()

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
        self.__manter_tela_aberta = True
        lista_opcoes = {'Pesquisar por Titulo': self.pesquisar_titulo, 'Pesquisar por Autor': self.pesquisar_autor, 'Pesquisar por Genero': self.pesquisar_genero, 'Voltar': self.fechar_tela_livro}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_livro.pesquisa_livros()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_livro.aviso_erro()
            else:
                funcao_escolhida()      

        self.__controlador_principal.abrir_tela_livro
    
    def pesquisar_titulo(self):
        existeLivro = False
        titulo_pesquisado = self.__tela_livro.pesquisa_titulo()
        encontrado = None
        

        for livro in self.__livros:
            if livro.titulo == titulo_pesquisado:
                existeLivro = True
                encontrado = livro
                break
        if existeLivro:
            titulo = livro.titulo
            autor = livro.autor.nome
            genero = livro.genero.nome
            dados_livro = [titulo, autor, genero]
            mostrar_livro = self.__tela_livro.mostra_livro(dados_livro)
            if mostrar_livro == None:
                self.pesquisar_livros()

    def pesquisar_autor(self):
        existeLivro = False
        autor_pesquisado = self.__tela_livro.pesquisa_autor()
        encontrados = []
        lista_titulos = []
        
        for livro in self.__livros:
            if livro.autor.nome == autor_pesquisado:
                existeLivro = True
                encontrados.append(livro)
        if existeLivro:
            for livro in encontrados:
                lista_titulos.append(livro.titulo)
                livro_escolhido = self.__tela_livro.lista_livros(lista_titulos)
            if livro_escolhido != None:
                for livro in encontrados:
                    if livro.titulo == livro_escolhido:
                        titulo = livro.titulo
                        autor = livro.autor.nome
                        genero = livro.genero.nome
                        dados_livro = [titulo, autor, genero]
                        mostrar_livro = self.__tela_livro.mostra_livro(dados_livro)
                        if mostrar_livro == None:
                            self.pesquisar_autor()

        self.pesquisar_livros()

    def pesquisar_genero(self):
        existeLivro = False
        genero_pesquisado = self.__tela_livro.pesquisa_genero()
        encontrados = []
        lista_titulos = []
        
        for livro in self.__livros:
            if livro.genero.nome == genero_pesquisado:
                existeLivro = True
                encontrados.append(livro)
        if existeLivro:
            for livro in encontrados:
                lista_titulos.append(livro.titulo)
                livro_escolhido = self.__tela_livro.lista_livros(lista_titulos)
            if livro_escolhido != None:
                for livro in encontrados:
                    if livro.titulo == livro_escolhido:
                        titulo = livro.titulo
                        autor = livro.autor.nome
                        genero = livro.genero.nome
                        dados_livro = [titulo, autor, genero]
                        mostrar_livro = self.__tela_livro.mostra_livro(dados_livro)
                        if mostrar_livro == None:
                            self.pesquisar_genero()

        self.pesquisar_livros()                   


    def verificar_analises(self):
        pass

    def verificar_notas(self):
        pass

    def fechar_tela_livro(self):
        self.__manter_tela_aberta = False