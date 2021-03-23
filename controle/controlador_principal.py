from limite.tela_principal import TelaPrincipal

class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()

    def inicializa_sistema(self):
        self.abre_tela()

    def livros(self):
        pass

    def usuarios(self):
        pass
        
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
    
        opcoes = {1: self.livros, 2: self.usuarios, 0: self.encerra_sistema}

        while True:

            opcao_escolhida = self.__tela_principal.menu_principal()

            funcao_escolhida = opcoes[opcao_escolhida]

            funcao_escolhida()
            
