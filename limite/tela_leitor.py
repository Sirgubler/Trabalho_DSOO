class TelaLeitor():

    def __init__(self):
        pass

    def menu_principal(self):
        print("----------Menu Leitor----------")
        print("1 - Selecionar Leitor")
        print("2 - Cadastrar Leitor")
        print("0 - Voltar")
        return int(input("Selecione a opção desejada: "))

    def selecao_de_leitor(self, leitores):
        if leitores != []:
            n = 1
            print("----------Leitores----------")
            for leitor in leitores:
                print('{} - {}'.format(n, leitor.nome))
                n += 1
            codigo_leitor = int(input("Selecione o leitor desejado: "))
            return leitores[codigo_leitor - 1]
        else:
            print('NENHUM LEITOR CADASTRADO!')