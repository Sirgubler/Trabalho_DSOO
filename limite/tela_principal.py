class TelaPrincipal():

    def __init__(self):
        pass

    #Opções gerais da classe ControladorPrincipal. É chamada pela função abrir_tela()
    def menu_principal(self):
        print("\n----------Menu Principal----------")
        print("1 - Menu Livros")
        print("2 - Menu Usuários")
        print("0 - Sair")
        return int(input("Selecione a opção desejada: "))

    #Opções de seleção de usuário. É chamada pela função abrir_tela_usuario()
    def menu_usuario(self):
        print("\n----------Menu Usuários----------")
        print("1 - Menu Leitor")
        print("2 - Menu Crítico")
        print("3 - Menu Admin")
        print("0 - Voltar")
        return int(input("Selecione a opção desejada: "))