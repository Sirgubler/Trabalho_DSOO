class TelaCritico():

    def __init__(self):
        pass

    def menu_principal(self):
        print("----------Menu Principal----------")
        print("1 - Menu Livros")
        print("2 - Menu Usuários")
        print("0 - Sair")
        return int(input("Selecione a opção desejada: "))

    def cadastro_de_critico(self):
        print('\n----------Cadastro de Crítico----------')
        return input('Digite o nome do Crítico: ')