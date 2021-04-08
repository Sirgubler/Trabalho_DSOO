from entidade.pessoa import Pessoa

class Critico(Pessoa):

    def __init__(self, nome: str, registro_profissional: int):
        super().__init__(nome)
        self.__registro_profissional = registro_profissional
        self.__login = None
        self.__senha = None

    @property
    def registro_profissional(self):
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional: int):
        self.__registro_profissional = registro_profissional

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login
    
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha