from entidade.livro import Livro
from limite.tela_livro import TelaLivro
from controle.controlador_autor import ControladorAutor
from controle.controlador_genero import ControladorGenero
from persistencia.livro_dao import LivroDAO
from excecao.nenhum_livro import NenhumLivro


class ControladorLivro():

    def __init__(self, controlador_principal):
        self.__tela_livro = TelaLivro()
        self.__controlador_autor = ControladorAutor(self)
        self.__controlador_genero = ControladorGenero(self)
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True
        self.__dao = LivroDAO()


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
            
            for livro in self.__dao.get_all():
                if livro.titulo == titulo:
                    naoexisteLivro = False
                    break
            if naoexisteLivro:
                livros = list(self.__dao.get_all())
                if livros == []:
                    codigo = 1
                else:
                    codigo = livros[-1].codigo + 1
                novo_livro = Livro(codigo, titulo, autor_escolhido, genero_escolhido)
                self.__dao.add(novo_livro)
        
        self.abrir_tela_livro()

    def alterar_livro(self):
        self.__manter_tela_aberta = True
        existeLivro = False
        titulo = self.__tela_livro.busca_titulo()
        livro_encontrado = None

        for livro in self.__dao.get_all():
            if livro.titulo == titulo:
                existeLivro = True
                livro_encontrado = livro
                break
        if existeLivro:
            self.__manter_tela_aberta = True
            lista_opcoes = {'Alterar Autor': self.altera_autor, 'Alterar Genero': self.altera_genero, 'Cancelar': self.fechar_tela_livro}
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
                        self.__dao.add(livro)
                else:
                    self.alterar_livro()      
        self.abrir_tela_livro()
    
    def altera_autor(self, livro_encontrado: Livro):
        novo_autor = self.__controlador_autor.alterar_autor_livro()
        livro_encontrado.autor = novo_autor

    def altera_genero(self, livro_encontrado):
        novo_genero = self.__controlador_genero.alterar_genero_livro()
        livro_encontrado.genero = novo_genero

    def listar_livros(self):
        livros = []

        for livro in self.__dao.get_all():
            livros.append(livro.titulo)
        if livros != []:
            livro_escolhido = self.__tela_livro.lista_livros(livros)
            if livro_escolhido != 'Voltar':
                self.mostrar_livro(livro_escolhido)
            else:
                self.abrir_tela_livro()
        else:
            assert NenhumLivro('Livro')
            self.abrir_tela_livro()

    def mostrar_livro(self, livro_escolhido):
        existeLivro = False        
        dados_livro = {}
        livro_encontrado = None

        for livro in self.__dao.get_all():
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

        for livro in self.__dao.get_all():
            if livro.titulo == titulo:
                naoexisteLivro = False
                self.__dao.remove(livro.codigo)
                self.__controlador_principal.remover(livro)
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

        self.abrir_tela_livro()
    
    def pesquisar_titulo(self):
        existeLivro = False
        titulo_pesquisado = self.__tela_livro.pesquisa_titulo()
        livro_encontrado = None

        if titulo_pesquisado != None:   
            for livro in self.__dao.get_all():
                if livro.titulo == titulo_pesquisado:
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
            else:
                self.__tela_livro.aviso_erro()

        self.pesquisar_livros()

    def pesquisar_autor(self):
        autor_pesquisado = self.__tela_livro.pesquisa_autor()
        livros_encontrado = []
        livros = []

        for livro in self.__dao.get_all():
            autor = livro.autor
            if autor.nome == autor_pesquisado:
                livros_encontrado.append(livro)
        if livros_encontrado != []:
            for livro in livros_encontrado:
                livros.append(livro.titulo)
            if livros != []:
                livro_escolhido = self.__tela_livro.lista_livros(livros)
                if livro_escolhido != None:
                    self.mostrar_livro(livro_escolhido)
                else:
                    self.pesquisar_livros()
            else:
                self.pesquisar_livros()
        
        self.pesquisar_livros()

    def pesquisar_genero(self):
        genero_pesquisado = self.__tela_livro.pesquisa_genero()
        livros_encontrado = []
        livros = []

        for livro in self.__dao.get_all():
            genero = livro.genero
            if genero.nome == genero_pesquisado:
                livros_encontrado.append(livro)
        if livros_encontrado != []:
            for livro in livros_encontrado:
                livros.append(livro.titulo)
            if livros != []:
                livro_escolhido = self.__tela_livro.lista_livros(livros)
                if livro_escolhido != None:
                    self.mostrar_livro(livro_escolhido)
                else:
                    self.pesquisar_livros()
            else:
                self.pesquisar_livros()
        
        self.pesquisar_livros()               


    def verificar_analises(self):
        livros = self.__controlador_principal.ver_analises_criticos()
        self.__tela_livro.mostra_analises(livros)


    def verificar_notas(self):
        livros = self.__controlador_principal.ver_notas_leitores()
        for livro in livros.keys():
            media = sum(livros[livro])/len(livros[livro])
            livros[livro] = media
        self.__tela_livro.mostra_notas(livros)

    def pesquisar_autor_livros(self):
        autor_pesquisado = self.__tela_livro.pesquisa_autor()
        livros_encontrado = []
        livros = []

        for livro in self.__dao.get_all():
            autor = livro.autor
            if autor.nome == autor_pesquisado:
                livros_encontrado.append(livro)
        if livros_encontrado != []:
            for livro in livros_encontrado:
                livros.append(livro.titulo)
            if livros != []:
                livro_escolhido = self.__tela_livro.lista_livros(livros)
                if livro_escolhido != 'Voltar':
                    self.mostrar_livro_autor(livro_escolhido)
                else:
                    self.__controlador_autor.pesquisar_autores()
            else:
                self.__controlador_autor.pesquisar_autores()
        
        self.__controlador_autor.pesquisar_autores()

    def pesquisar_genero_livros(self):
        genero_pesquisado = self.__tela_livro.pesquisa_genero()
        livros_encontrado = []
        livros = []

        for livro in self.__dao.get_all():
            genero = livro.genero
            if genero.nome == genero_pesquisado:
                livros_encontrado.append(livro)
        if livros_encontrado != []:
            for livro in livros_encontrado:
                livros.append(livro.titulo)
            if livros != []:
                livro_escolhido = self.__tela_livro.lista_livros(livros)
                if livro_escolhido != 'Voltar':
                    self.mostrar_livro_genero(livro_escolhido)
                else:
                    self.__controlador_genero.pesquisar_generos()
            else:
                self.__controlador_genero.pesquisar_generos()
        
        self.__controlador_genero.pesquisar_generos()

    def pesquisar_genero_autores(self):
        genero_pesquisado = self.__tela_livro.pesquisa_genero()
        livros_encontrado = []
        autores = []
        titulos = []

        for livro in self.__dao.get_all():
            genero = livro.genero
            if genero.nome == genero_pesquisado:
                livros_encontrado.append(livro)
        if livros_encontrado != []:
            for livro in livros_encontrado:
                autor = livro.autor
                nome_autor = autor.nome
                autores.append(nome_autor)
            if autores != []:
                lista_final = set(autores)
                autor_escolhido = self.__tela_livro.lista_autores(lista_final)
                if autor_escolhido != None:
                    for livro in livros_encontrado:
                        autor_objeto = livro.autor
                        if autor_objeto.nome == autor_escolhido:
                            titulos.append(livro.titulo)
                    mostrando = self.__tela_livro.mostra_autor(titulos)
                    if mostrando == 'Voltar':
                        titulos = []
                        self.pesquisar_genero_autores

        self.__controlador_genero.pesquisar_generos()

    def mostrar_livro_genero(self, livro_escolhido):
        existeLivro = False        
        dados_livro = {}
        livro_encontrado = None

        for livro in self.__dao.get_all():
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

    def mostrar_livro_autor(self, livro_escolhido):
        existeLivro = False        
        dados_livro = {}
        livro_encontrado = None

        for livro in self.__dao.get_all():
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

    def pesquisar_autor_generos(self):
        autor_pesquisado = self.__tela_livro.pesquisa_autor()
        livros_encontrado = []
        generos = []
        titulos = []

        for livro in self.__dao.get_all():
            autor = livro.autor
            if autor.nome == autor_pesquisado:
                livros_encontrado.append(livro)
        if livros_encontrado != []:
            for livro in livros_encontrado:
                genero = livro.genero
                nome_genero = genero.nome
                generos.append(nome_genero)
            if generos != []:
                lista_final = set(generos)
                genero_escolhido = self.__tela_livro.lista_generos(lista_final)
                if genero_escolhido != None:
                    for livro in livros_encontrado:
                        genero_objeto = livro.genero
                        if genero_objeto.nome == genero_escolhido:
                            titulos.append(livro.titulo)
                    mostrando = self.__tela_livro.mostra_genero(titulos)
                    if mostrando == 'Voltar':
                        titulos = []
                        self.pesquisar_autor_generos

        self.__controlador_autor.pesquisar_autores()

    def remove_autor(self, nome: str):
        autor_deletado = self.__controlador_autor.autor_deletado()

        for livro in self.__dao.get_all():
            objeto_autor = livro.autor
            if objeto_autor.nome == nome:
                livro.autor = autor_deletado

    def selecionar_livro(self):
        livros = []
        livro_objeto = None

        for livro in self.__dao.get_all():
            livros.append(livro.titulo)
        if livros != []:
            livro_escolhido = self.__tela_livro.lista_livros(livros)
            if livro_escolhido != 'Voltar':
                for livro in self.__dao.get_all():
                    if livro.titulo == livro_escolhido:
                        livro_objeto = livro
        
        return livro_objeto
    
    def sincronia_autor(self, autor_encontrado, nome):
        for livro in self.__dao.get_all():
            if livro.autor == autor_encontrado:
                autor_do_livro = livro.autor
                autor_do_livro.nome = nome

    def sincronia_genero(self, genero_encontrado, nome):
        for livro in self.__dao.get_all():
            if livro.genero == genero_encontrado:
                genero_do_livro = livro.genero
                genero_do_livro.nome =  nome  
                
    def fechar_tela_livro(self):
        self.__manter_tela_aberta = False
