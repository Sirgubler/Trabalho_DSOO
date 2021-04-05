class TelaLeitor():

    def __init__(self):
        pass

    #Opções gerais da classe Leitor. É chamada pela função abrir_tela_leitor() 
    def menu_principal(self):
        while True:
            print("\n----------Menu Leitores----------")
            print("1 - Selecionar Leitor")
            print("2 - Cadastrar Leitor")
            print("0 - Voltar")
            try:
                return int(input('Selecione a opção desejada: '))
            except Exception:
                print('ERRO!\nDigite apenas números!')

    def selecao_de_leitor(self, leitores):
        while True:
            if leitores != []:
                while True:
                    n = 1
                    print("\n----------Leitores----------")
                    for leitor in leitores:
                        print('{} - {}'.format(n, leitor))
                        n += 1
                    print('0 - Voltar')
                    try:
                        return int(input('Selecione a opção desejada: '))
                    except Exception:
                        print('ERRO!\nDigite apenas números!')
            else:
                print('Nenhum leitor cadastrado!')
                return None

    def cadastro_de_leitor(self):
        print('\n----------Cadastro de Leitor----------')
        return input('Digite o nome do leitor: ')

    def inclusao_de_livro_lido(self):
        livro = input('Selecione Livro: ')
        try:
            nota = int(input('Nota: '))
        except Exception:
            print('ERRO!\nDigite apenas números!')
        else:
            return [livro, nota]

    #Opções específicas do leitor. É chamada pela função abrir_menu_leitor()
    def menu_leitor(self, nome):
        while True:
            print('\n----------Menu Leitor----------')
            print('Leitor: {}'.format(nome))
            print('1 - Ver livros lidos')
            print('2 - Incluir um livro lido')
            print('0 - Voltar')
            try:
                return int(input('Selecione a opção desejada: '))
            except Exception:
                print('ERRO!\nDigite apenas números!')

    def livros_lidos(self, livros_lidos):
        if livros_lidos != {}:
            print('\n----------Livros Lidos----------')
            for livro in livros_lidos:
                print('{}: {}'.format(livro, livros_lidos[livro]))
        else:
            print('Nenhum livro lido!')

    def aviso_erro(self, tipo):
        if type(tipo) == int:
            print('ERRO!\nDigite um valor válido!')
        elif type(tipo) == str:
            print('ERRO!\nLeitor já cadastrado!')
