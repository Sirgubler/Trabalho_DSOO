class TelaPrincipal():

    def __init__(self):
        pass

    def menu_principal(self):
        print("----------Menu Principal----------")
        print("1 - Menu Livros")
        print("2 - Menu Usuários")
        print("0 - Sair")
        return int(input("Selecione a opção desejada: "))

    def menu_usuario(self):
        print("----------Menu Usuários----------")
        print("1 - Menu Leitor")
        print("2 - Menu Crítico")
        print("3 - Menu Admin")
        print("0 - Voltar")
        return int(input("Selecione a opção desejada: "))