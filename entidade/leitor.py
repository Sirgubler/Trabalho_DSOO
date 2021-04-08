from entidade.pessoa import Pessoa

class Leitor(Pessoa):

    def __init__(self, nome: str):
        super().__init__(nome)

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