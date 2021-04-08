from limite.tela_sistema import TelaSistema

class ControladorSistema:

    def __init__(self, controlador_principal):
        self.__tela_sistema = TelaSistema()
        self.__controlador_principal = controlador_principal
        self.__manter_tela_aberta = True

    def abrir_tela_sistema(self):
        pass

    def fechar_tela(self):
        self.__manter_tela_aberta = False