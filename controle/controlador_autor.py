from entidade.autor import Autor
from limite.tela_autor import TelaAutor

class ControladorAutor: 

    def __init__(self, controlador_livro):        
        self.__autores = []
        self.__tela_autor = TelaAutor()
        self.__controlador_livro = controlador_livro
        self.__manter_tela_aberta = True

    def autores(self):
        return self.autores

    def naoexisteAutor(self, nome: str):
        naoexisteAutor = True
        autor_enviado = None

        for autor in self.__autores:
            if autor.nome == nome:
                naoexisteAutor = False
                autor_enviado = autor
                break
        if naoexisteAutor:
            novo_autor = Autor(nome)
            self.__autores.append(novo_autor)
            autor_enviado = novo_autor
        
        return autor_enviado
    
    def pega_nome(self, autor: Autor):
        nome = autor.nome
        return nome

    def alterar_autor_livro(self):
        naoexisteAutor = True
        nome = self.__tela_autor.altera_autor_livro()

        for autor in self.__autores:
            if autor.nome == nome:
                novo_autor = autor
                naoexisteAutor = False
                break
        if naoexisteAutor:
            novo_autor = Autor(nome)
            self.__autores.append(novo_autor)

        return novo_autor

    def abrir_tela_autor(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {'Cadastrar Autor': self.cadastrar_autor, 'Alterar Autor': self.alterar_autor, 'Listar Autores': self.listar_autores, 'Remover Autor': self.remover_autor, 'Pesquisar Autores': self.pesquisar_autores, 'Voltar': self.fechar_tela_autor}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_autor.menu_autor()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_autor.aviso_erro()
            else:
                funcao_escolhida()      

        self.__controlador_livro.abrir_tela_livro()

    def cadastrar_autor(self):
        naoexisteAutor = True
        nome = self.__tela_autor.cadastra_autor()
        
        if nome != None:
            for autor in self.__autores:
                if autor.nome == nome:
                    naoexisteAutor = False
                    break
            if naoexisteAutor:
                novo_autor = Autor(nome)
                self.__autores.append(novo_autor)
        
        self.abrir_tela_autor()

    def alterar_autor(self):
        existeAutor = False
        autor_alterado = self.__tela_autor.altera_autor()
        autor_encontrado = None

        for autor in self.__autores:
            if autor.nome == autor_alterado:
                existeAutor = True
                autor_encontrado = autor
                break
        if existeAutor:
            novo_nome = self.__tela_autor.alteracao()
            if novo_nome != None:
                autor_encontrado.nome = novo_nome
            else:
                self.abrir_tela_autor()
        
        self.abrir_tela_autor()

    def listar_autores(self):
        autores = []

        for autor in self.__autores:
            autores.append(autor.nome)

        autor_escolhido = self.__tela_autor.lista_autores(autores)
        if autor_escolhido != 'Voltar':
            self.mostrar_autor(autor_escolhido)
        else:
            self.abrir_tela_autor()

    def mostrar_autor(self, autor_escolhido):
        existeAutor = False        
        dados_autor = {}
        autor_encontrado = None

        for autor in self.__autores:
            if autor.nome == autor_escolhido:
                existeAutor = True
                autor_encontrado = autor
                break
        if existeAutor:
            nome = autor_encontrado.nome
            dados_autor = {'nome': nome}
            self.__tela_autor.mostra_autor(dados_autor)
           
        self.abrir_tela_autor()
    
    def remover_autor(self):
        existeAutor = False
        nome = self.__tela_autor.remove_autor()
        autor_encontrado = None

        if nome != None:
            for autor in self.__autores:
                if autor.nome == nome:
                    existeAutor = True
                    autor_encontrado = autor
                    break
            if existeAutor:
                self.__controlador_livro.remove_autor(nome)
                self.__autores.remove(autor_encontrado)
            else:
                self.__tela_autor.aviso_erro()

        self.abrir_tela_autor()   

    def pesquisar_autores(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {'Pesquisar Livros do Autor': self.pesquisar_titulo, 'Pesquisar Generos do Autor': self.pesquisar_generos, 'Voltar': self.fechar_tela_autor}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_autor.pesquisa_autores()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_autor.aviso_erro()
            else:
                funcao_escolhida()      

        self.abrir_tela_autor()
    
    def pesquisar_titulo(self):
        self.__controlador_livro.pesquisar_autor_livros()

    def pesquisar_generos(self):
        self.__controlador_livro.pesquisar_autor_generos()

    def fechar_tela_autor(self):
        self.__manter_tela_aberta = False
    
    def autor_deletado(self):
        nome = 'Autor Deletado'
        autor_deletado = Autor(nome)

        return autor_deletado