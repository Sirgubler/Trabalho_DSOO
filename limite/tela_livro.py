class TelaLivro():
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("---------- LIVROS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Livro")
        print("2 - Remover Livro")
        print("3 - Listar Livros")
        print("4 - Pesquisar Livro por Titulo")
        print("5 - Ver Analises")
        print("6 - Nota")
        print("0 - Retornar")

        opcao = int(input("Selecione a opção desejada: "))
        return opcao

    def cadastro_livro(self):
        print("-------- CADASTRO DE LIVRO --------")
        nome = input("DIGITE O TITULO DO LIVRO: ")
        autor = input("DIGITE O AUTOR DO LIVRO: ")
        genero = input("DIGITE O GENERO DO LIVRO: ")

        return {"nome": nome, "autor": autor, "genero": genero}

    def exclusao_livro(self):
        print("-------- EXCLUSAO DE LIVRO --------")
        nome = input("DIGITE O TITULO DO LIVRO: ")
        autor = input("DIGITE O AUTOR DO LIVRO: ")
        genero = input("DIGITE O GENERO DO LIVRO: ")

        return {"nome": nome, "autor": autor, "genero": genero}
    
    def mostra_livro(self, dados_livro):
        print("-------- INFORMACOES DESTE LIVRO ABAIXO -------")
        print("NOME DO LIVRO: ", dados_livro["nome"])
        print("AUTOR DO LIVRO: ", dados_livro["autor"])
        print("GENERO DO LIVRO: ", dados_livro["genero"])
        
    def pega_nome_livro(self, nome_do_livro):
        print("-------- NOME DO LIVRO --------")
        nome = input("Nome: ")

        return {"nome": nome}

    def pesquisar_livro(self):
        print("-------- BUSCA DE LIVRO POR TITULO --------")
        nome = input("DIGITE O NOME DO LIVRO QUE DESEJA BUSCAR: ")

        return {"nome": nome}

    def mostra_analise(self, dados_analise):
        print("-------- INFORMACOES DA CRITICA --------") 
        print("CRITICA FEITA: ", dados_analise["analise"])
        print("REALIZADA PARA O LIVRO: ", dados_analise["livro"])

    def mostra_nota(self, dados_da_nota):
        print("-------- INFORMACOES DA AVALIACAO --------")
        print("NOTA DA AVALIACAO: ", dados_da_nota["nota"])
        print("REALIZADA PARA O LIVRO: ", dados_da_nota["livro"])