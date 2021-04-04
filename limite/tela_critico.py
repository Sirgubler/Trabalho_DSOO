class TelaCritico():

    def __init__(self):
        pass

    #Opções gerais da classe Critico. É chamada pela função abrir_tela_critico()
    def menu_principal(self):
        print("----------Menu Principal----------")
        print("1 - Selecionar Critico")
        print("0 - Sair")
        return int(input("Selecione a opção desejada: "))

    def selecao_de_critico(self, criticos):
        if criticos != []:
            n = 1
            print("\n----------criticos----------")
            for critico in criticos:
                print('{} - {}'.format(n, critico))
                n += 1
            print('0 - Voltar')
            return int(input("Selecione o critico desejado: "))
        else:
            print('NENHUM critico CADASTRADO!')

    def cadastro_de_critico(self):
        print('\n----------Cadastro de critico----------')
        return input('Digite o nome do critico: ')

    def inclusao_de_livro_analisado(self):
        livro = input('Selecione Livro: ')
        analise = str(input('Analise: '))
        return [livro, analise]

    #Opções específicas do critico. É chamada pela função abrir_menu_critico()
    def menu_critico(self, nome):
        print('\n----------Menu critico----------')
        print('critico: {}'.format(nome))
        print('1 - Ver livros analisados')
        print('2 - Incluir um livro analisado')
        print('0 - Voltar')
        return int(input('Selecione a opção desejada: '))

    def livros_analisados(self, livros_analisados):
        print('\n----------Livros analisados----------')
        for livro in livros_analisados:
            print('{}: {}'.format(livro, livros_analisados[livro]))

    def aviso_erro(self, tipo):
        if type(tipo) == int:
            print('ERRO!\nDigite um valor válido!')
        elif type(tipo) == str:
            print('ERRO!\nCrítico já cadastrado!')
