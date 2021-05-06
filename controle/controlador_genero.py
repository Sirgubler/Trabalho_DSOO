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

        for genero in self.__generos:
            if genero.nome == nome:
                naoexisteGenero = False
                break
        if naoexisteGenero:
            novo_genero = Genero(nome)
            self.__generos.append(novo_genero)

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
        pass

    def alterar_genero(self):
        pass

    def listar_generos(self):
        pass
    
    def remover_genero(self):
        pass

    def pesquisar_generos(self):
        pass

    def fechar_tela_genero(self):
        self.__manter_tela_aberta = False