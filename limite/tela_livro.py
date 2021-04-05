class TelaLivro():

    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- MENU LIVROS --------")
        print("Opcoes disponiveis relacionadas a livro")
        print("1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Remover Livro")
        print("4 - Pesquisar Livro por Titulo")
        print("5 - Pesquisar Livros por Autor")
        print("6 - Pesquisar Livros por Genero")
        print("7 - Ver Analises")
        print("8 - Verificar Notas")
        print("9 - Menu Autor")
        print("10 - Menu genero")
        print("0 - Retornar")
        try:
            return int(input("Selecione uma opcao : "))
        except Exception:
            print('ERRO!\nDigite apenas números!')


    def cadastro_livro(self):
        print("-------- CADASTRO DE LIVRO --------")
        titulo = input("DIGITE O TITULO DO LIVRO QUE DESEJA CADASTRAR: ")

        return titulo

    def mostra_livro(self, dados_livro):
        print("-------- INFORMAÇOES DE LIVRO REGISTRADO -------")
        print("TITULO DO LIVRO: ", dados_livro['titulo'])
        print("AUTOR DO LIVRO: ", dados_livro['autor'])
        print("GENERO DO LIVRO: ", dados_livro['genero'])

    def exclusao_livro(self):
        print("-------- EXCLUSAO DE LIVRO --------")
        titulo = input("DIGITE O TITULO DO LIVRO QUE DESEJA EXCLUIR: ")

        return titulo
    
    def pesquisa_titulo(self):
        print("-------- PESQUISA DE LIVRO POR TITULO --------")
        titulo = input("DIGITE O TITULO DO LIVRO QUE DESEJA BUSCAR SOBRE: ")
        
        return titulo

    def pesquisa_autor(self):
        print("-------- PESQUISA DE LIVRO POR AUTOR --------")
        autor = input("DIGITE O NOME DO AUTOR QUE DESEJA VER OS LIVROS ESCRITOS: ")

        return autor

    def pesquisa_genero(self):
        print("-------- PESQUISA DE LIVRO POR GENERO --------")
        genero = input("DIGITE O GENERO QUE DESEJA VER LIVROS RELACIONADOS: ")

        return genero

    def sucesso_registro(self):
        print("O LIVRO FOI REGISTRADO COM SUCESSO!")

    def falha_registro(self):
        print("O LIVRO JA ESTA REGISTRADO!")

    def falha_exclusao(self):
        print("O LIVRO NAO CONSTA NOS REGISTROS!")

    def falha_busca(self):
        print("NAO FORAM ENCONTRADOS REGISTROS")

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')