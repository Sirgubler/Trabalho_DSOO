from entidade.pessoa import Pessoa

class Leitor(Pessoa):

    def __init__(self, nome: str):
        super().__init__(nome)
#        self.__analises = []

#    @property
#    def analises(self):
#        return self.__analises

#    @analises.setter
#    def analises(self, analises: list):
#        self.__analises = analises

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

#    def adicionar_analise(self, analise: Analise):
#        self.__analises.append(analise)