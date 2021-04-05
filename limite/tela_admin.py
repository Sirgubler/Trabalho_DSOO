class TelaAdmin():

    def __init__(self):
        pass

    def menu_principal(self):
        print("\n----------Menu Admin----------")
        print("1 - Cadastrar Crítico")
        print("0 - Voltar")
        try:
            return int(input('Selecione a opção desejada: '))
        except Exception:
            print('ERRO!\nDigite apenas números!')

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')
