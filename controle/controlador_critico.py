from limite.tela_critico import TelaCritico
from entidade.critico import Critico

class ControladorCritico():
    
    def __init__(self, controlador_principal):
        self.criticos = []
        self.__tela_critico = TelaCritico()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    