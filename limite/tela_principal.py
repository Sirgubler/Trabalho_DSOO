class TelaPrincipal():

    def __init__(self):
        pass

    def menu_principal(self):
        while True:
            print("----------Menu Principal----------")
            print("1 - Menu Livros")
            print("2 - Menu Usuários")
            print("0 - Sair")
            try:
                return int(input("Selecione a opção desejada: "))
            except Exception:
                print('ERRO!\nDigite apenas números!')  

    def menu_usuario(self):
        while True:
            print("----------Menu Usuários----------")
            print("1 - Menu Leitor")
            print("2 - Menu Crítico")
            print("3 - Menu Admin")
            print("0 - Voltar")
            try:
                return int(input("Selecione a opção desejada: "))
            except Exception:
                print('ERRO!\nDigite apenas números!')

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')