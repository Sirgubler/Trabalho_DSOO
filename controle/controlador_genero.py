from entidade.genero import Genero
from limite.tela_genero import TelaGenero

class ControladorGenero: 

    def __init__(self, controlador_livro):        
        self.__generos = []
        self.__tela_genero = TelaGenero()
        self.__controlador_livro = controlador_livro
        self.__manter_tela_aberta = True

    def generos(self):
        return self.__generos

    def naoexisteGenero(self, nome: str):
        naoexisteGenero = True
        genero_enviado = None

        for genero in self.__generos:
            if genero.nome == nome:
                naoexisteGenero = False
                genero_enviado = genero
                break
        if naoexisteGenero:
            novo_genero = Genero(nome)
            self.__generos.append(novo_genero)
            genero_enviado = novo_genero
        
        return genero_enviado
    
    def pega_nome(self, genero: Genero):
        nome = genero.nome
        return nome

    def alterar_genero_livro(self):
        naoexisteGenero = True
        nome = self.__tela_genero.altera_genero_livro()

        for genero in self.__generos:
            if genero.nome == nome:
                naoexisteGenero = False
                novo_genero = genero
                break
        if naoexisteGenero:
            novo_genero = Genero(nome)
            self.__generos.append(novo_genero)

        return novo_genero

    def abrir_tela_genero(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {'Cadastrar Genero': self.cadastrar_genero, 'Alterar Genero': self.alterar_genero, 'Listar Generos': self.listar_generos, 'Remover Genero': self.remover_genero, 'Pesquisar Generos': self.pesquisar_generos, 'Voltar': self.fechar_tela_genero}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_genero.menu_genero()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_genero.aviso_erro()
            else:
                funcao_escolhida()      

        self.__controlador_livro.abrir_tela_livro()

    def cadastrar_genero(self):
        naoexisteGenero = True
        nome = self.__tela_genero.cadastra_genero()
        
        if nome != None:
            for genero in self.__generos:
                if genero.nome == nome:
                    naoexisteGenero = False
                    break
            if naoexisteGenero:
                novo_genero = Genero(nome)
                self.__generos.append(novo_genero)
        
        self.abrir_tela_genero()

    def alterar_genero(self):
        existeGenero = False
        genero_alterado = self.__tela_genero.altera_genero()
        genero_encontrado = None

        for genero in self.__generos:
            if genero.nome == genero_alterado:
                existeGenero = True
                genero_encontrado = genero
                break
        if existeGenero:
            novo_nome = self.__tela_genero.alteracao()
            if novo_nome != None:
                genero_encontrado.nome = novo_nome
            else:
                self.abrir_tela_genero()
        
        self.abrir_tela_genero()

    def listar_generos(self):
        generos = []

        for genero in self.__generos:
            generos.append(genero.nome)

        genero_escolhido = self.__tela_genero.lista_generos(generos)
        
        if genero_escolhido == 'Voltar':
            self.abrir_tela_genero()

    def mostrar_genero(self, genero_escolhido):
        existeGenero = False        
        dados_genero = {}
        genero_encontrado = None

        for genero in self.__generos:
            if genero.nome == genero_escolhido:
                existeGenero = True
                genero_encontrado = genero
                break
        if existeGenero:
            nome = genero_encontrado.nome
            dados_genero = {'nome': nome}
            self.__tela_genero.mostra_genero(dados_genero)
           
        self.abrir_tela_genero()
    
    def remover_genero(self):
        existeGenero = False
        nome = self.__tela_genero.remove_genero()
        genero_encontrado = None

        if nome != None:
            for genero in self.__generos:
                if genero.nome == nome:
                    existeGenero = True
                    genero_encontrado = genero
                    break
            if existeGenero:
                self.__controlador_livro.remove_genero(nome)
                self.__generos.remove(genero_encontrado)
            else:
                self.__tela_genero.aviso_erro()

        self.abrir_tela_genero()   

    def pesquisar_generos(self):
        self.__manter_tela_aberta = True
        lista_opcoes = {'Pesquisar Livros do Genero': self.pesquisar_titulo, 'Pesquisar Autores do Genero': self.pesquisar_autores, 'Voltar': self.fechar_tela_genero}
        while self.__manter_tela_aberta:
            opcao_escolhida = self.__tela_genero.pesquisa_generos()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
            except Exception:
                self.__tela_genero.aviso_erro()
            else:
                funcao_escolhida()      

        self.abrir_tela_genero()
 
    def pesquisar_titulo(self):
        self.__controlador_livro.pesquisar_genero_livros()

    def pesquisar_autores(self):
        self.__controlador_livro.pesquisar_genero_autores()

    def fechar_tela_genero(self):
        self.__manter_tela_aberta = False

    def genero_deletado(self):
        nome = 'Autor Deletado'
        genero_deletado = Genero(nome)

        return genero_deletado