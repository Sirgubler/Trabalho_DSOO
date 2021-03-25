class TelaLeitor():

    def __init__(self):
        pass

    def menu_principal(self):
        print("----------Menu Leitores----------")
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
            print('0 - Voltar')
            return int(input("Selecione o leitor desejado: "))
        else:
            print('NENHUM LEITOR CADASTRADO!')

    def cadastro_de_leitor(self):
        print('----------Cadastro de Leitor----------')
        return input('Digite o nome do leitor: ')

    def menu_leitor(self, nome):
        print('----------Menu Leitor----------')
        print('Leitor: {}'.format(nome))
        print('1 - Ver livros lidos')
        print('2 - Incluir um livro lido')
        print('0 - Voltar')
        return int(input('Selecione a opção desejada: '))
