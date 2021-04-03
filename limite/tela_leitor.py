class TelaLeitor():

    def __init__(self):
        pass

    #Opções gerais da classe Leitor. É chamada pela função abrir_tela_leitor() 
    def menu_principal(self):
        print("\n----------Menu Leitores----------")
        print("1 - Selecionar Leitor")
        print("2 - Cadastrar Leitor")
        print("0 - Voltar")
        return int(input("Selecione a opção desejada: "))

    def selecao_de_leitor(self, leitores):
        if leitores != []:
            n = 1
            print("\n----------Leitores----------")
            for leitor in leitores:
                print('{} - {}'.format(n, leitor))
                n += 1
            print('0 - Voltar')
            return int(input("Selecione o leitor desejado: "))
        else:
            print('NENHUM LEITOR CADASTRADO!')

    def cadastro_de_leitor(self):
        print('\n----------Cadastro de Leitor----------')
        return input('Digite o nome do leitor: ')

    def inclusao_de_livro_lido(self):
        livro = input('Selecione Livro: ')
        nota = int(input('Nota: '))
        return [livro, nota]

    #Opções específicas do leitor. É chamada pela função abrir_menu_leitor()
    def menu_leitor(self, nome):
        print('\n----------Menu Leitor----------')
        print('Leitor: {}'.format(nome))
        print('1 - Ver livros lidos')
        print('2 - Incluir um livro lido')
        print('0 - Voltar')
        return int(input('Selecione a opção desejada: '))

    def livros_lidos(self, livros_lidos):
        print('\n----------Livros Lidos----------')
        for livro in livros_lidos:
            print('{}: {}'.format(livro, livros_lidos[livro]))
